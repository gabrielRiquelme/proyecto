select aes_encrypt('micontraseña','key');

select aes_decrypt(aes_encrypt('micontraseña','key'),'key');

select md5('micontraseña');

select sha('micontraseña');

Select sha2('micontraseña',224);