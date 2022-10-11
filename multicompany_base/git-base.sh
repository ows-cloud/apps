source git-config.sh
cd $path_odoo

git checkout $branch_all
git diff $branch_main $branch_all > $patch_all
COMMIT_ID=$(git rev-parse --verify HEAD)
git checkout $branch_base
git cherry-pick $COMMIT_ID
git diff $branch_main $branch_base > $patch_base
git checkout $branch_all
