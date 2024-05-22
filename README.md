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
NoSQL can take several forms due to its dynamic nature, but one form in particular is the idea of key-value pairs. This resembles dictionaries in Python or name-value pairs for JSON. A demonstration of NoSQL in another form can be seen below, taking the form of a document.

<img src="SQL_NoSQL_comparison.png" alt="Comparison image to show key-value pairs within NoSQL as a schema design." width="600"/> [2]

If it can be organised into a form as simple as this, it can work with NoSQL.

## Scalability in NoSQL

In SQL scalability is vertical, meaning a more packed load of querying and storage will need a better machine to handle the database. This is fine for a small project that can handle the higher demand, but for many cases this is unwarranted. With NoSQL, it is thankfully less stressful to increase the load of the system due to its horizontal scalability. This implies that larger work loads can be handled by separating the load amongst multiple servers in a process known as "sharding". This is great as it does end up being more efficient than getting one more powerful machine, the work that multiple servers can do ending up being more usable and getting an overall larger outcome than vertical scaling, but it can still have some caveats. For instance, servers can be quite expensive still (even if cheaper than the alternative), plus the need to have all these servers connected in some form can be annoying when newer servers will have to find a way to communicate with older models, along with the allocation of what exactly each server will do for different segments. To many though, these downsides are nothing compared to the hassle of maintaining information on a single system. [3], [4]

A horizontal form of scalability is sometimes just referred to as "scalable", which does make sense when you consider how much less restrictive this set-up is compared to vertical scaling.

## NoSQL Databases

NoSQL is a way of presenting databases that can take many forms. It can be as simple as the aforementioned key-value pairs, or it can be closer to the form of SQL (tables). The forms typically seen in various databases are:
- Key-value pairs
- Document-based (as seen in the schema design example image)
- Wide-column
- Graph
- Time series

Wide-column acts quite like a database that you might see within SQL, but with the major difference that columns are used to house the data rather than rows. Columns that are connected are under a collected "column family", meaning there is a connection in their attributes where this is necessary.

The graph form has a use of nodes connecting points of the data that have a specific relationship within the database. This is one of the more complex forms of NoSQL, yet it still serves the same purpose. Whatever form of the database is chosen all depends on what is most viable for the project. [5]



## MongoDB
While perhaps not the preferred choice for many, this introduction to NoSQL will now go through introducing MongoDB, a database product for NoSQL which mainly focuses on the document form of NoSQL databases. Some things MongoDB does are similar, though not exactly the same, to how SQL does them. For example, in SQL multiple groups of data are separated and labelled via tables. MongoDB can also do this for organisation, but instead of tables it uses what are known as "collections". The document form of NoSQL that MongoDB utilises also simply allows for these documents it uses to hold within them all related data, resulting in what should be a faster reading speed for data as opposed to the tabular structure of SQL. [6]

## The Architecture of MongoDB
MongoDB is structured in a particular way to theoretically get the best efficiency in performance and flexibility. In an abbreviated list, this architecture is as follows:
1. Collection - a group of documents for MongoDB
2. Document - where data is kept in MongoDB, using Binary JSON (BSON)
3. Database - where all of the collections are held
4. Shard - An application of the horizontal scaling of NoSQL, shards are used to partition data across multiple nodes (or servers)
5. Replica Set - A group of nodes or servers that hold identical data, useful for backups or if the data needs to be manipulated in various different ways
6. Query Router - Where the user (or client) has information obtained for them based on the query they input, which determines the path to the data requested and, if necessary, which shard to be directed to
7. Configuration servers - Where configuration settings for the instance of MongoDB being utilised for a database are stored



#### Sources
[1] "SQL vs NoSQL: 5 Critical Differences", as of 22/05/2024 - https://www.integrate.io/blog/the-sql-vs-nosql-difference/

[2] https://medium.com/tech-tajawal/nosql-modeling-database-structuring-part-ii-4c364c4bc17a

[3] https://www.datacamp.com/blog/sql-vs-nosql-databases

[4] https://www.cloudzero.com/blog/horizontal-vs-vertical-scaling/

[5] https://docs.aws.amazon.com/whitepapers/latest/choosing-an-aws-nosql-database/types-of-nosql-databases.html

[6] https://www.w3schools.com/mongodb/mongodb_get_started.php

[7] 
