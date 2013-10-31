

JS9   = ../js9
JS9JS = $(JS9)/js/fits-stream

all: 	$(JS9)/js9fits-stream.html	\
	$(JS9JS)/fits-stream.js

$(JS9)/js9fits-stream.html: js9fits-stream.html
	cp -p js9fits-stream.html $(JS9)/js9fits-stream.html

$(JS9JS)/fits-stream.js: fits-stream.js
	#browserify -r ./fits-stream | uglifyjs > $(JS9JS)/fits-stream.js
	browserify -r ./fits-stream   > $(JS9JS)/fits-stream.js

