# Understanding NoSQL

The concept of NoSQL (also known as Not Only SQL) is an alternative to SQL (Structured Query Language). However, despite the name, NoSQL doesn't completely throw out the concept of structure in how its presented - implied by its alias. The concept is more to have a freeform, dynamic design while addressing some of the more troublesome parts of regular SQL. 

## Comparing SQL and NoSQL
In general, we can summarise the comparisons between SQL and NoSQL into a table.


|Feature     |SQL                   |NoSQL                     |
| ------     | ------               | ------                   |
|Type        |Relational            |Non-Relational            |
|Languages   |MySQL, SQLServer, etc.|Python, C#, MongoDB, etc. |
|Design      |"Table Design"        |Dynamic                   |
|Scalability |Vertical              |Horizontal                |

By non-relational, we mean a form of database storage that does not rely on them being associated with primary and foreign keys or (specifically) tables, concepts more attributed to relational databases. Design (or schema design) is the form it takes in visualising the concept. SQL is has a "table design" because upon looking at information within SQL it presents itself as just that, tables. NoSQL on the other hand has a lot more forms it can take, which we will look into, along with the differences in scalability and what this means. NoSQL ends up being great for JSON and data, stuff that appears more unstructured, whereas SQL is always best still for stuff that needs that extra structure to function correctly - perhaps a fixed list of chain locations and opening times for businesses. [1]

## NoSQL Schema Design
NoSQL can take several forms due to its dynamic nature, but one form in particular is the idea of key-value pairs. This resembles dictionaries in Python or name-value pairs for JSON. A demonstration of this can be seen below, and shows perhaps one of the furthest forms of NoSQL from resembling SQL.

<img src="SQL_NoSQL_comparison.png" alt="Comparison image to show key-value pairs within NoSQL as a schema design." width="600"/> [2]

If it can be organised into a form as simple as this, it can work with NoSQL.

## Scalability in NoSQL

In SQL scalability is vertical, meaning a more packed load of querying and storage will need a better machine to handle the database. This is fine for a small project that can handle the higher demand, but for many cases this is unwarranted. With NoSQL, it is thankfully less stressful to increase the load of the system due to its horizontal scalability. This implies that larger work loads can be handled by separating the load amongst multiple servers in a process known as "sharding". This is great as it does end up being more efficient than getting one more powerful machine, the work that multiple servers can do ending up being more usable and getting an overall larger outcome than vertical scaling, but it can still have some caveats. For instance, servers can be quite expensive still, plus the need to have all these servers connected in some form.


#### Sources
[1] https://www.integrate.io/blog/the-sql-vs-nosql-difference/

[2] https://medium.com/tech-tajawal/nosql-modeling-database-structuring-part-ii-4c364c4bc17a
