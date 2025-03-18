#!/bin/bash
exec > >(sudo tee -a /var/log/ghrunner_install.log) 2>&1
set -x

sudo apt -y update
sudo apt install -y zip

function install_packages() {
    sudo apt install -y jq
}
install_packages

# Declare variables
RUNNER_URL="${RUNNER_URL}"
RUNNER_SHA="${RUNNER_SHA}"
RUNNER_TAR="${RUNNER_TAR}"
GITHUB_PAT_TOKEN="${TOKEN}"
OWNER="mosesugwu"
REPO="Cloud-Engineer"
USER_HOME="/home/mosesugwu"
USER="mosesugwu"
RUNNER_DIR="/actions-runner"


# Debug: Print variables
echo "RUNNER_URL: ${RUNNER_URL}"
echo "RUNNER_SHA: ${RUNNER_SHA}"
echo "RUNNER_TAR: ${RUNNER_TAR}"
echo "TOKEN: ${TOKEN}"


# Create a folder and navigate into it
mkdir -p "$HOME/actions-runner"
cd "$HOME/actions-runner"
echo $PWD


curl -o actions-runner-linux-x64-2.322.0.tar.gz -L "${RUNNER_URL}"
echo "${RUNNER_SHA}  actions-runner-linux-x64-2.322.0.tar.gz" | shasum -a 256 -c
tar xzf "${RUNNER_TAR}"

curl -L -X POST -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer ${TOKEN}" -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/repos/$OWNER/$REPO/actions/runners/registration-token > response.json 


# Ensure response.json is owned by the current user
sudo chown $USER:$USER response.json

RUNNER_TOKEN=$(jq -r '.token' response.json)
echo "RUNNER_TOKEN: $RUNNER_TOKEN"

# Run the configuration script with automated inputs
echo "Running GitHub Actions runner configuration"

# Ensure all files and directories have correct ownership before configuration
sudo chown -R $USER:$USER "$RUNNER_DIR"

# Run the configuration script as the user (not with sudo)
sudo -u mosesugwu bash <<EOF
cd $RUNNER_DIR
./config.sh --url https://github.com/$OWNER/$REPO --token $RUNNER_TOKEN --name ghrunner-vm02 --labels self-hosted,Linux,X64,ghrunner-vm02 --runnergroup Default
# ./config.sh --url https://github.com/$OWNER/$REPO --token $RUNNER_TOKEN <<EOL
# mosesugwu Default Runner Group
# ghrunner-vm02
# self-hosted,Linux,X64,ghrunner-vm02
# _work
# EOL
EOF

./run.sh &

# Ensure correct ownership before installing the service
sudo chown -R $USER:$USER "$RUNNER_DIR"

./svc.sh install
./svc.sh start

# Debug: List files to ensure correct ownership and presence of svc.sh
ls -la

# Check if the service is running
sudo systemctl status actions.runner.$OWNER-$REPO.ghrunner-vm02.service
















