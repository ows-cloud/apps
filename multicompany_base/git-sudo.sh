source git-config.sh
cd $path_odoo

git checkout $branch_all
git diff $branch_sudo $branch_all > $patch_all
COMMIT_ID=$(git rev-parse --verify HEAD)
git checkout $branch_sudo
git cherry-pick $COMMIT_ID
git diff $branch_main $branch_sudo > $patch_sudo
git checkout $branch_all
