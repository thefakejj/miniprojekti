CREATE TABLE IF NOT EXISTS reference 
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
reftype TEXT NOT NULL,
username TEXT, 
key TEXT NOT NULL, 
author TEXT, 
title TEXT, 
year INTEGER, 
publisher TEXT,
volume TEXT,
series TEXT,
address TEXT,
edition TEXT,
month TEXT,
note TEXT,
school TEXT,
type TEXT
);
