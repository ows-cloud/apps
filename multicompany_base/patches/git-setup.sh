source git-config.sh
cd $path_odoo
git reset --hard
git clean -f

git checkout $branch_main
git branch -D $branch_base
git checkout -b $branch_base
git apply $patch_base
git add -A
git commit -m $patch_base

git checkout $branch_main
git branch -D $branch_sudo
git checkout -b $branch_sudo
git apply $patch_sudo
git add -A
git commit -m $patch_sudo

git checkout $branch_main
git branch -D $branch_all
git checkout -b $branch_all
git apply $patch_all
git add -A
git commit -m $patch_all
