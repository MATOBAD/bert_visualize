FROM nvidia/cuda:10.1-devel-ubuntu18.04
COPY requirements.txt japanese_tokenization.py ./ 
RUN apt update && \
    apt install -y --no-install-recommends curl unzip locales g++ gcc cmake && \
    curl -sSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -bfp /usr/local && \
    rm -rf /tmp/miniconda.sh && \
    conda update conda && \
    pip install -r requirements.txt && \ 
    cp japanese_tokenization.py /usr/local/lib/python3.7/site-packages/transformers && \
    curl -sSL https://github.com/ku-nlp/jumanpp/releases/download/v2.0.0-rc3/jumanpp-2.0.0-rc3.tar.xz -o jumanpp-2.0.0-rc3.tar.xz && \
    tar xf jumanpp-2.0.0-rc3.tar.xz && \
    cd jumanpp-2.0.0-rc3 && \
    mkdir bld && \
    cd bld && \
    cmake .. -DCMAKE_BUILD_TYPE=Release && \
    make install -j && \
    rm -rf jumanpp-2.0.0-rc3.tar.xz && \
    curl -sSL http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/JapaneseBertPretrainedModel/Japanese_L-12_H-768_A-12_E-30_BPE_transformers.zip -o /tmp/Japanese_L-12_H-768_A-12_E-30_BPE_transformers.zip && \
    curl -sSL http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/JapaneseBertPretrainedModel/Japanese_L-12_H-768_A-12_E-30_BPE_WWM_transformers.zip -o /tmp/Japanese_L-12_H-768_A-12_E-30_BPE_WWM_transformers.zip && \
    mkdir /bert && \
    unzip /tmp/Japanese_L-12_H-768_A-12_E-30_BPE_transformers.zip -d /bert && \
    unzip /tmp/Japanese_L-12_H-768_A-12_E-30_BPE_WWM_transformers.zip -d /bert && \
    rm /tmp/Japanese_L-12_H-768_A-12_E-30_BPE_transformers.zip && \ 
    rm /tmp/Japanese_L-12_H-768_A-12_E-30_BPE_WWM_transformers.zip && \ 
    conda clean --all --yes && \
    locale-gen ja_JP.UTF-8 && \
    localedef -f UTF-8 -i ja_JP ja_JP && \
    apt remove -y --purge unzip g++ cmake curl && \
    apt -y clean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log
ENV LANG ja_JP.UTF-8 
ENV LANGUAGE jja_JP:jp 
ENV LC_ALL ja_JP.UTF-8
