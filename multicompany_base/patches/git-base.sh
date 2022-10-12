source git-config.sh
cd $path_odoo

# The last commit in the ALL branch:
# - Apply to the BASE branch.
# - Update the ALL patch and the BASE patch, and commit them.
git checkout $branch_all
COMMIT_ID=$(git rev-parse --verify HEAD)
COMMIT_MESSAGE=$(git log -1 --pretty=format:%B)
git checkout $branch_base
git cherry-pick $COMMIT_ID
git diff $branch_main $branch_base > $patch_base
git checkout $branch_all
git diff $branch_main $branch_all > $patch_all

cd $path_patches
git add ./*
git commit -m "$COMMIT_MESSAGE"
