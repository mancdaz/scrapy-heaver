DROP TABLE IF EXISTS snickers;
CREATE TABLE snickers(
  guid CHAR(32) PRIMARY KEY,
  item_num TEXT,
  item_name TEXT,
  item_color_num TEXT,
  item_colour_desc TEXT,
  item_link TEXT,
  item_desc TEXT,
  item_features TEXT,
  item_sizes TEXT,
  item_addl_info TEXT,
  image_urls TEXT,
  updated DATETIME
) DEFAULT CHARSET=utf8;
