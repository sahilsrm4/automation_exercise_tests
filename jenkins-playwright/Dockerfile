FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-venv \
        curl \
        wget \
        ca-certificates \
        && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --break-system-packages playwright

RUN python3 -m playwright install --with-deps chromium

USER jenkins