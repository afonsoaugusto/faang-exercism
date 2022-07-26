# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.241.1/containers/alpine/.devcontainer/base.Dockerfile

# [Choice] Alpine version: 3.15, 3.14, 3.13
ARG VARIANT="3.15"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-alpine-${VARIANT}

# ** [Optional] Uncomment this section to install additional packages. **
RUN apk add \
        go==1.18.3-r1 \
        python3==3.9.7-r4 \
        py3-pip==22.1.2-r0 \
        --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community
RUN apk update \
    && apk add --no-cache \
        elixir==1.12.2-r0 \
        make==4.3-r0
RUN wget https://github.com/exercism/cli/releases/download/v3.0.13/exercism-3.0.13-linux-x86_64.tar.gz && \
    tar -xf exercism-3.0.13-linux-x86_64.tar.gz -C /usr/local/bin


