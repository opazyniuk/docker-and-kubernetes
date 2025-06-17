CREATE TABLE IF NOT EXISTS quotes (
    id SERIAL PRIMARY KEY,
    quote TEXT NOT NULL,
    work_title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO quotes (quote, work_title, author) VALUES
    ('In the souls of the people the grapes of wrath are filling and growing heavy, growing heavy for the vintage.', 'The Grapes of Wrath', 'John Steinbeck'),
    ('A journey is a person in itself; no two are alike. And all plans, safeguards, policing, and coercion are fruitless. We find that after years of struggle that we do not take a trip; a trip takes us.', 'Travels with Charley: In Search of America', 'John Steinbeck'),
    ('Adjust the flower, adorn the bower, make sweet the honeyed hour.', 'Of Mice and Men', 'John Steinbeck'),
    ('And now that you don''t have to be perfect, you can be good.', 'East of Eden', 'John Steinbeck'),
    ('What good is the warmth of summer, without the cold of winter to give it sweetness.', 'The Winter of Our Discontent', 'John Steinbeck'),
    ('The free, exploring mind of the individual human is the most valuable thing in the world.', 'East of Eden', 'John Steinbeck'),
    ('We are lonesome animals. We spend all our life trying to be less lonesome.', 'The Winter of Our Discontent', 'John Steinbeck'),
    ('It seems to me that if you or I must choose between two courses of thought or action, we should remember our dying and try so to live that our death brings no pleasure on the world.', 'Nobel Prize Speech', 'John Steinbeck'),
    ('Ideas are like rabbits. You get a couple and learn how to handle them, and pretty soon you have a dozen.', 'Journal of a Novel: The East of Eden Letters', 'John Steinbeck'),
    ('A sad soul can kill quicker than a germ.', 'How to Tell Good Guys From Bad Guys', 'John Steinbeck'); 
    