#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from os import path
from wordcloud import WordCloud

words = [
    (u'#!/bin/bash', 2),
    (u'#!/bin/sh', 3),
    (u'#!/usr/bin/env python', 2),
    (u'#!/usr/bin/perl -w', 2),
    (u'#ifdef DEBUG', 1),
    (u'!', 3),
    (u'|', 3),
    (u'+', 3),
    (u'-', 3),
    (u'.bashrc', 3),
    (u'.emacs', 3),
    (u'.zshrc', 3),
    (u'/etc', 5),
    (u'/etc/init.d/sshd', 2),
    (u'/etc/init.d/httpd', 2),
    (u'/etc/init.d/ftpd', 2),
    (u'/etc/init.d/ntpd', 2),
    (u'/etc/init.d/bos', 2),
    (u'/etc/passwd', 3),
    (u'/etc/rc.conf', 3),
    (u'/opt/local', 3),
    (u'/usr', 4),
    (u'/usr/home', 3),
    (u'/usr/local', 3),
    (u'/var', 4),
    (u'/var/log', 3),
    (u'1978', 5),
    (u'64', 4),
    (u'64', 3),
    (u'6502', 3),
    (u'68k', 5),
    (u'8', 3),
    (u':-)', 4),
    (u';-)', 4),
    (u'?', 3),
    (u'AFS', 9),
    (u'AFS', 5),
    (u'AFS', 3),
    (u'ARM', 5),
    (u'AUTOEXEC.BAT', 1),
    (u'AlexMUD', 2),
    (u'Android', 7),
    (u'Arduino', 4),
    (u'Arla', 6),
    (u'BIOS', 4),
    (u'BSD 4.3', 3),
    (u'Baltikumprojektet', 3),
    (u'Berkley Source Distribution', 2),
    (u'BitTorrent', 3),
    (u'C++', 10),
    (u'CPU', 4),
    (u'Cascading Style Sheets', 2),
    (u'Centos', 6),
    (u'Chrome', 4),
    (u'Coca Cola', 6),
    (u'Common Lisp', 2),
    (u'DIGITAL', 7),
    (u'DNS', 10),
    (u'Debian', 9),
    (u'Donald Knuth', 5),
    (u'ETLA', 5),
    (u'Fedora', 7),
    (u'Firefox', 4),
    (u'FreeBSD', 8),
    (u'GLFW', 6),
    (u'GNU on VMS', 2),
    (u'GNU', 11),
    (u'HTTP/2', 8),
    (u'Hacker', 3),
    (u'HashMap', 3),
    (u'HyperText Transfer Protocol', 2),
    (u'HyperText Markup Language', 2),
    (u'I/O', 5),
    (u'IPMI', 3),
    (u'IPv6', 5),
    (u'ISO-8859-1', 2),
    (u'ISO-8859-15', 2),
    (u'Java', 5),
    (u'KTH', 17),
    (u'Kerberos', 14),
    (u'LAN', 5),
    (u'Linux', 14),
    (u'Linux', 10),
    (u'Linux', 6),
    (u'Linux', 2),
    (u'Mountain Dew', 4),
    (u'NetBSD', 2),
    (u'OSX', 9),
    (u'Open Source', 10),
    (u'OpenBSD', 7),
    (u'OpenGL', 6),
    (u'OpenSSL', 7),
    (u'OpenVMS', 5),
    (u'OpenVMS', 5),
    (u'Out of band management', 1),
    (u'PDF', 8),
    (u'PDP/11', 6),
    (u'PostIt', 5),
    (u'Q', 16),
    (u'Q-huset', 11),
    (u'RHEL', 5),
    (u'Raspberry Pi', 4),
    (u'Ruby', 8),
    (u'Rust', 8),
    (u'SATA', 5),
    (u'SCSI', 5),
    (u'SIP', 4),
    (u'SQL', 10),
    (u'Solaris', 6),
    (u'Stacken', 20),
    (u'Stacken', 30),
    (u'Stacken', 40),
    (u'Stacken', 50),
    (u'Stackenföreläsning', 16),
    (u'Stackpointer', 5),
    (u'Stockholm', 10),
    (u'Sun', 5),
    (u'TCP/IP', 5),
    (u'THS', 7),
    (u'TLA', 5),
    (u'Tcl/Tk', 2),
    (u'Tekniska Högskolans Studentkår', 4),
    (u'The Art of Computer Programming', 2),
    (u'Torsdag', 30),
    (u'TreeMap', 5),
    (u'Tru64', 5),
    (u'Ubuntu', 5),
    (u'UNIX Network Programming', 2),
    (u'Unix System V', 3),
    (u'Unix', 18),
    (u'VMS', 5),
    (u'Vax', 5),
    (u'WAN', 5),
    (u'WPA', 6),
    (u'Webkit', 3),
    (u'Wikipedia', 5),
    (u'Windows', 5),
    (u'X', 5),
    (u'X11', 5),
    (u'X11R6', 6),
    (u'YXA', 4),
    (u'abstraktion', 3),
    (u'assembler', 5),
    (u'atomklocka', 3),
    (u'automake', 1),
    (u'autoconf', 1),
    (u'awk', 3),
    (u'bash', 5),
    (u'binary', 3),
    (u'bit', 3),
    (u'bitar', 2),
    (u'block', 3),
    (u'blockrepresentation', 2),
    (u'byte', 5),
    (u'c', 5),
    (u'c++', 7),
    (u'carbon', 5),
    (u'cargo run --release', 2),
    (u'ceph', 5),
    (u'cisco', 5),
    (u'clojure', 5),
    (u'closure', 5),
    (u'cluster', 5),
    (u'code', 12),
    (u'command', 5),
    (u'compiler', 5),
    (u'couchdb', 4),
    (u'csh', 5),
    (u'css', 9),
    (u'cvs', 4),
    (u'damm', 1),
    (u'dator', 5),
    (u'datorer', 3),
    (u'datorarkeologi', 6),
    (u'datorförening', 16),
    (u'datorförening', 14),
    (u'datorförening', 12),
    (u'datorhall', 15),
    (u'datorhall', 13),
    (u'datorhall', 11),
    (u'demoprogrammering', 4),
    (u'device', 5),
    (u'diskchassi', 5),
    (u'diskuterar', 5),
    (u'docker', 7),
    (u'elixir', 6),
    (u'emacs', 9),
    (u'eps', 5),
    (u'erlang', 5),
    (u'fil', 5),
    (u'fish', 4),
    (u'foo bar baz', 1),
    (u'foo bar', 2),
    (u'foo', 3),
    (u'fork()', 4),
    (u'fprintf()', 4),
    (u'fulhack', 2),
    (u'funktionell programmering', 2),
    (u'fågelbur', 1),
    (u'git', 9),
    (u'github', 8),
    (u'glusterfs', 7),
    (u'grep', 5),
    (u'groff', 5),
    (u'h2o', 5),
    (u'hack', 5),
    (u'haskell', 4),
    (u'heimdal', 15),
    (u'html', 7),
    (u'html5', 7),
    (u'http', 6),
    (u'https', 6),
    (u'hårddisk', 6),
    (u'hårdvara', 14),
    (u'höstmöte', 5),
    (u'iOS', 5),
    (u'imap', 7),
    (u'int main(argc, argv)', 3),
    (u'int', 5),
    (u'interface', 5),
    (u'internet', 10),
    (u'java', 7),
    (u'javascript', 6),
    (u'jpeg', 5),
    (u'json', 5),
    (u'kaffe', 11),
    (u'katalog', 5),
    (u'kerberos', 16),
    (u'klient', 5),
    (u'kompilator', 11),
    (u'kryptografi', 9),
    (u'kvantdator', 5),
    (u'kylskåp', 11),
    (u'kårförening', 4),
    (u'kårförening', 3),
    (u'kårförening', 2),
    (u'kårförening', 1),
    (u'language', 5),
    (u'lekstugan', 5),
    (u'lisp', 8),
    (u'lokal', 12),
    (u'machine', 5),
    (u'main()', 5),
    (u'make install', 3),
    (u'make world', 4),
    (u"make: don't know how to make love. Stop.", 1),
    (u'minecraft', 3),
    (u'minne', 5),
    (u'mkdir', 3),
    (u'monotone', 5),
    (u'mp3', 5),
    (u'mud', 5),
    (u'mysql', 8),
    (u'netvärk', 1),
    (u'node.js', 5),
    (u'nosql', 4),
    (u'nroff', 5),
    (u'ntp', 8),
    (u'nuccc', 3),
    (u'nätverk', 5),
    (u'obegripligt', 1),
    (u'obfuskerad', 5),
    (u'objektorienterad', 5),
    (u'ogg', 5),
    (u'operativsystem', 11),
    (u'optimering', 5),
    (u'packa', 5),
    (u'papegoja', 5),
    (u'parrot', 5),
    (u'pdf', 5),
    (u'pdp', 9),
    (u'perl', 6),
    (u'pipe()', 5),
    (u'png', 5),
    (u'postfix', 11),
    (u'postgresql', 9),
    (u'postscript', 7),
    (u'prestanda', 5),
    (u'primtal', 5),
    (u'processor', 7),
    (u'programmering', 13),
    (u'ps', 5),
    (u'python', 7),
    (u'rackmontering', 7),
    (u'raytracer', 5),
    (u'rcs', 5),
    (u'REST', 5),
    (u'router', 6),
    (u'rtfm', 2),
    (u'ruby', 7),
    (u'rust', 7),
    (u'scheme', 5),
    (u'sed', 5),
    (u'segvara', 5),
    (u'sendmail.cf', 4),
    (u'server', 9),
    (u'sh', 5),
    (u'showpage', 4),
    (u'soffa', 16),
    (u'sort', 5),
    (u'source', 5),
    (u'ssh', 10),
    (u'stacken@stacken.kth.se', 12),
    (u'stackomaten', 14),
    (u'stackomaten', 6),
    (u'storage', 5), 
    (u'styrelsen@stacken.kth.se', 3),
    (u'sushi', 8),
    (u'swift', 5),
    (u'systemadministration', 6),
    (u'te', 5),
    (u'textigenkänning', 5),
    (u'tiff', 5),
    (u'troff', 5),
    (u'trådlös', 5),
    (u'utf8', 5),
    (u'ux', 5),
    (u'vi', 5),
    (u'vim', 5),
    (u'virtualisering', 5),
    (u'void', 5),
    (u'vorbis', 5),
    (u'vårmöte', 5),
    (u'web', 5),
    (u'whiteboard', 5),
    (u'wiki', 5),
    (u'www.Stacken.KTH.se', 10),
    (u'x86', 5),
    (u'xml', 5),
    (u'zones', 5),
    (u'zsh', 6),
]

bigsize = 1
allwords = words
# Snyggare, men _mycket_ tyngre att rita.
#bigsize = 15;
#allwords = [(w, s*bigsize) for w, s in words] + words + words

print "Making a cloud of %d words." % len(allwords)

s = 8 * bigsize
wordcloud = WordCloud(width=60*s, height=200*s, max_font_size=13 * s,
                      relative_scaling=.5).fit_words(words)

image = wordcloud.to_image()
image.save('image.png')