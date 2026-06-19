CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price INT NOT NULL
);

INSERT INTO products (name, price) VALUES
  ('Docker Sticker', 100),
  ('Compose Mug', 350),
  ('CI/CD Notebook', 250);
