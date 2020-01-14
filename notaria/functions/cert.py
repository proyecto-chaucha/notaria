from notaria.models.cert import cert_model
from notaria.functions.crypto import sha3_hex
from werkzeug.utils import secure_filename
from notaria import db
from flask import flash


def process_file(username, form):
	filename = secure_filename(form.document.data.filename)
	content = form.document.data.stream.read()
	size = len(content)
	sha3 = sha3_hex(str(content))

	if size > 0 and len(filename) > 0:
		flash("%s (%.2f kb) subido exitosamente" % (filename, size/1024))

		file = cert_model(username=username, filename=filename, size=size, sha3=sha3)
		db.session.add(file)
		db.session.commit()

		return True
	else:
		return False