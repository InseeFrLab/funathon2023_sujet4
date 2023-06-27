WORK_DIR="/home/onyxia/work"

# Clone project repository
git clone --depth 1 https://github.com/InseeFrLab/funathon2023_sujet4.git
chown -R onyxia:users "${WORK_DIR}/funathon2023_sujet4"

# Install system libraries
apt-get update && apt-get install ffmpeg libsm6 libxext6 libzbar0 -y

# Install Python dependencies
pip install -r "${WORK_DIR}/funathon2023_sujet4/requirements.txt"

# Open the relevant notebook when starting Jupyter Lab
jupyter server --generate-config
echo "c.LabApp.default_url = '/lab/tree/work/funathon2023_sujet4/index.ipynb'" >> /home/onyxia/.jupyter/jupyter_server_config.py
