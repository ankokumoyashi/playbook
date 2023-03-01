FROM python:3.10-buster
RUN pip3 install --upgrade pip
RUN pip3 install numpy cython pystan
RUN pip3 install cmdstanpy[all]
RUN python3 -c 'import cmdstanpy; cmdstanpy.install_cmdstan()'

WORKDIR /workdir
