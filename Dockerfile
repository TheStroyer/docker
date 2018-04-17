FROM ibmcom/websphere-traditional:9.0.0.7-install

COPY /assets/ /home

COPY /profile/was9-lex-profile.car /home/was

COPY /scripts /work