FROM ubuntu:latest

# Install packages
RUN apt-get update \
    && apt-get install -y \
        python3.8 \
        python3-pip \
        git \
        ruby \
        ruby-dev \
        curl
# Install Pip packages
RUN pip3 install \
    cfn-lint

# Install Ruby Gems
RUN gem install \
    cfn_nag

# Install AWS CLI V2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install
