FROM alpine
RUN apk update
RUN apk upgrade
RUN apk add ca-certificates 
RUN apk update ca-certificates
RUN apk add --update tzdata
RUN rm -rf /var/cache/apk/*
COPY simple.sh /script.sh
CMD ["/script.sh"]
