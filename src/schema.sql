CREATE TABLE IF NOT EXISTS reference 
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
reftype TEXT NOT NULL,
username TEXT, 
key TEXT NOT NULL, 
author TEXT NOT NULL, 
title TEXT NOT NULL, 
year INTEGER NOT NULL, 
publisher TEXT NOT NULL,
volume TEXT,
series TEXT,
address TEXT,
edition TEXT,
month TEXT,
note TEXT,
school TEXT NOT NULL,
type TEXT
);
