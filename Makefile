

JS9   = ../js9
JS9JS = $(JS9)/js/fits-stream

all: 	$(JS9)/js9fits-stream.html

$(JS9)/js9fits-stream.html: js9fits-stream.html
	cp -p js9fits-stream.html $(JS9)/js9fits-stream.html

