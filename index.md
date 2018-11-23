**Inspiration**
- Who is the most collaborative Billboard Chart musician in the past 50
years?

- Which year had the most collaborations?

- Which artist was the most collaborative in 2017?

- What is the longest ‘chain’ of collaborations in our dataframe?

 **Background**
 
In modern music, collaborations seem more popular than ever. As an aspiring musician, it is easy to gain attention by working with someone with an established career and fan base by ‘featuring’ them on your song. The ‘featured’ artist is typically paid upfront, which can be a more desirable form of income than having to worry about records sale and tour dates. By analyzing such collaborations in the Billboard Top 100 Charts from the past 50 years to present, we aim to better understand the nature of how and why musicians work together.

We defined a collaboration as two or more artists appearing in the ARTIST column of our dataframe. We then constructed a simple undirected graph with artists as our vertices and edges representing the collaborations between them. The degree of any vertex then shows the total number of unique collaborations that artist has done. This way, when two artists work together it only adds one to each of their total collaboration counts, and repeat edges are not allowed.

**Data set:**

We used BeautifulSoup to scrape data from ULTIMATE MUSIC DATABASE (umdmusic.com). Example webpage:
http://www.umdmusic.com/default.asp?Lang=English&Chart=D
We stored data from 1967 - 2018 in csv format, which included: {‘ARTIST’, ‘TITLE’, ‘ENTRY DATE’, ‘ENTRY POSITION’, ‘PEAK POSITION’, ‘TOTAL WEEKS’}. We used the overall statistics opposed to the weekly statistics when constructing our dataframe.
 
**Methodology**

The data in csv format is transformed into pandas dataframe to analyze the data
and to create graphs. Since graphs only need the names of the artists in the songs to figure out the nodes and the edges, the ‘ARTIST’ column in the dataframe gets extracted into its own variable X. The strings in X contain either single artist name or multiple artists names, separated by conjunction word ‘and,’ or punctuations such as ‘/’ ‘,’ or words like ‘feature’ ‘feat.’ and other conjunction substring, the ‘split_string’ variable in the script has the list of separators to splits the strings with multiple artists. Strings with multiple artists holds a valuable information, the connection between two or more artists can be represented as the edges of the graph.

The number of combination of 2 artists chosen from total number of artists in the song gives all possible combination of 2 artists in the song without repeat. However, to remove duplicate collaboration, i.e., two same artists collaborate in multiple songs, the edges are added into a set. The set may contain duplicate collaboration that has artists swap position in the tuple, i.e., (‘J Cole’, ‘KiLL Edward’) and (‘KiLL Edward’, ‘J Cole’), but the duplicate has no issue with creating a valid graph. The nodes are the set of all artists in the edges.

The python library NetworkX produces a graph given a list of nodes and a list of tuple edges. It also has standard graph algorithms such as finding a cycle, which was used to find the longest cycle in the graph. Although, NetworkX has the capability to produce complex graphs, it does not have tools to render an interactive and neat graph visualization for presentation. Holoview, a library made on top of Bokeh, which is an interactive visualization library, is used to visualize the graph.

The most collaborative artist is the node with the highest degree. The most collaborative year has the highest number of edges in that year. The most collaborative artist in 2017 has the highest degree in 2017. The longest ‘chain’ of collaborations in the dataframe has the longest cycle in the graph. The NetworkX function nx.cycle_basis(G, root) returns a list of cycles in G that start at root. To find the longest ‘chain’ of collaborations we called nx.cycle_basis() on the 1,000 nodes with the highest degree. Each nodes returned a list of cycles, and only the largest is kept. It is then a simple matter to sort and find the cycle with the highest length.

**Results**

The artist with the highest number of unique collaborations is LIL WAYNE. Dwanyne Micheal Carter Jr (LIL WAYNE) began his career at 17 in 1999, and has been active in the rap community ever since. He put up an impressive 75 unique collaborations, the next highest being CHRIS BROWN at 56. It has been 5 years since LIL WAYNE released a solo album, but he has kept relevant by appearing as a feature on tracks from artists such as DRAKE, KODAK BLACK, and NICKI MINAJ. On average, songs with (#1) LIL WAYNE enter at spot #65, peak at spot #38 and stay in the charts for 16.5 weeks. These averages are consistent with the other top 10 most collaborative artists. (#4) KANYE WEST had the highest average peak at #34. (#8) NICKI MINAJ had the highest average entry at #61. (#5) LUDACRIS takes the title for artist with longest average weeks in the charts at 17.87. LIL WANYE’s statistics are very close to the top in all variables; we can conclude that if you want your song to succeed in the billboard charts, then you should definitely book LIL WAYNE for a feature.
 
Main graph:

[Check the interactive main graph](https://sunil07t.github.io/Exploring-Collaborations-in-the-Billboard-Charts/graph.html "Check the interactive main graph")
 
<img src="https://sunil07t.github.io/Exploring-Collaborations-in-the-Billboard-Charts/graph.png" width="50%" height="50%">

>This graph contains 2,674 nodes, and 2481 edges, and spans 1967-2018. Its shape is reminiscent of a cluster galaxy, with the highest concentration of nodes being at the center, surrounded by a ring of smaller groups of collaborators. LIL WAYNE is found in the center mass, along with all of the other top collaborators.

Lil Wayne's node:

<img src="https://sunil07t.github.io/Exploring-Collaborations-in-the-Billboard-Charts/lil_wayne_node.png" width="50%" height="50%">

>This is the main graph, but focused in on LIL WAYNE. He has degree 75, which is insane. Our study concludes that LIL WAYNE is the most collaborative popular musician of all time. Here is the complete list of his collaborators: 'PLIES', 'ENRIQUE IGLESIAS', 'JAY SEAN', 'BIG SEAN', 'KODAK BLACK', 'JUVENILE', 'EMINEM', 'BIRDMAN', 'RICK ROSS', 'GAME', 'PAUL WALL', 'YO GOTTI', 'LOGIC', 'MANNY FRESH', 'WIZ KHALIFA', 'JAY Z', 'T.I.', 'TANK', 'B.O.B', 'STATIC MAJOR', 'MACK MAINE', 'MACK 10', 'JENNIFER LOPEZ', 'SWIZZ BEATZ', 'CORY GUNZ', 'NICKI MINAJ', 'TOO SH', 'USHER', 'CHANCE THE RAPPER', 'WYCLEF JEAN', 'KEVIN RUDOLF', 'GORILLA ZOE', 'MICKEY', 'T PAIN', 'KANYE WEST', 'JUICY J', 'JHENE AIKO', 'YOUNG JEEZY', 'BRUNO MARS', 'IMAGINE DRAGONS', 'BEYONCE', 'CHRIS BROWN', 'AKON', 'MIKE POSNER', 'THE GAME', 'FRENCH MONTANA', 'FAT JOE', 'DRAKE', 'ARIANA GRANDE', 'PITBULL', 'BABY', 'KERI HILSON', 'PLAYAZ CIRCLE', 'SHAKIRA', 'BUSTA RHYMES', 'DETAIL', 'TY DOLL', 'DAVID GUETTA', 'NIIA', 'RICK ROS', 'DJ KHALED', 'ANDRE 3000', '2 CHAINZ', 'KELLY ROWLAND', 'BIRDMAN ', 'FUTURE', 'LLOYD', 'TYGA', 'BOBBY VALENTINO', 'FRENCH MONTANA or', 'CHARLIE PUTH', 'RICH GANG', 'KEYSHIA COLE', 'JOE BUDDEN', 'MEEK MILL'

The year with the most collaborations was last year, 2017 with 204 songs. The top 4 after 2017 were 2015 with 175, 2013 with 174, 2010 with 167, and 2012 with 166. The least collaborative years were 1994 and 1995 with 20, and 1990 with 18. It is interesting to note that 1969 had 97 songs, and 2001 had 107, making the relationship between year and number of collaborative songs unclear.
 
 Collaborations by year:
 
<img src="https://sunil07t.github.io/Exploring-Collaborations-in-the-Billboard-Charts/colabs_by_year.png" width="50%" height="50%">

>The collaboration by years bar graph shows the number of collaboration each year. After 1995 the average number of collaboration is growing. 

2017 graph:

[Check the interactive 2017 graph](https://sunil07t.github.io/Exploring-Collaborations-in-the-Billboard-Charts/2017_graph.html "Check the interactive 2017 graph")

<img src="https://sunil07t.github.io/Exploring-Collaborations-in-the-Billboard-Charts/2017_graph.png" width="50%" height="50%">

>The above graph is collaboration of 2017. It is interesting to see the similarity between this graph with the the main graph. Satellite collaborations on the side and a complex network in the middle.

The artist with the highest number of unique collaborations last year was QUAVO with 16. QUAVO is a member of the group MIGOS, and entered the industry in 2009. On average, songs with QUAVO enter the charts at #66, peaked at #45 and stayed for 16.4 weeks. QUAVO does not have any solo albums and seems to be taking full advantage of the popularity of his group MIGOS to make quick cash from features.
 
 Quavo's node:
 
<img src="https://sunil07t.github.io/Exploring-Collaborations-in-the-Billboard-Charts/Quavo.png" width="50%" height="50%">

>This is our 2017 graph, but focused in on QUAVO. He has degree 16. Like LIL WAYNE, QUAVO’s node is located in the center of the graph, where the highest concentration of artists exists. Here is the complete list of his collaborators: 'MAJOR LAZER', 'POST MALONE', 'TRAVIS SCOTT', '21 SAVAGE', 'QUALITY CONTROL', 'TAKEOFF', 'LIAM PAYNE', 'METRO BOOMIN', 'CAMILA CABELLO', '2 CHAINZ', 'JUSTIN BIEBER', 'DRAKE', 'OFFSET', 'CHANCE THE RAPPER', 'DJ KHALED', 'GUCCI MANE'

Our cycle graphs shows how musicians from completely different genres and eras are connected by those whom they collaborate with. While rapper SCHOOLBOY Q may never have met 'ZEDD' the dj, our cycle shows that we can connect them. Our cycle ranges from classics RONALD ISLEY, BRYAN ADAMS and BARBRA STREISAND, to modern artists KENDRICK LAMAR, 21 SAVAGE and GUCCI MANE. It reveals that the legend MICHAEL JACKSON is just 10 steps away from the new hit female rapper CARDI B. By examining cycles in our graph, we can explore the degrees of separation between artists and find unexpected connections such as those listed above. 

Longest cycle:

[Check the interactive longest cycle graph](https://sunil07t.github.io/Exploring-Collaborations-in-the-Billboard-Charts/largest_cycle_graph.html "Check the interactive longest cycle graph")

<img src="https://sunil07t.github.io/Exploring-Collaborations-in-the-Billboard-Charts/cycle.png" width="50%" height="50%">

>This cycle contains 77 nodes and spans multiple genres and musical eras. 
Here is the complete list: 
'E 40', 'YO GOTTI', 'A BOOGIE WIT DA HOODIE', 'KODAK BLACK', 'FRENCH MONTANA', 'SWAE LEE', 'KHALID', 'ALESSIA CARA', 'ZEDD', 'HAILEE STEINFELD', 'FLORIDA GEORGIA LINE', 'LUKE BRYAN', 'ERIC CHURCH', 'KEITH URBAN', 'BRAD PAISLEY', 'ALISON KRAUSS', 'KENNY ROGERS', 'KIM CARNES', 'BARBRA STREISAND', 'BRYAN ADAMS', 'ROD STEWART', 'RONALD ISLEY', 'WARREN G', 'MACK 10', 'BABY', 'MANNIE FRESH', 'CHAMILLIONAIRE', 'CIARA', 'FIELD MOB', 'JAMIE FOXX', 'THE DREAM', 'FABOLOUS', 'LIL MO', 'ANGIE MARTINEZ', 'KELIS', 'BUSTA RHYMES', 'JANET JACKSON', 'MICHAEL JACKSON', 'DIANA ROSS', 'MARVIN GAYE', 'ERICK SERMON', 'REDMAN', 'MASTER P', 'MO', 'IGGY AZALEA', 'BRITNEY SPEARS', 'G EAZY', 'CARDI B', '21 SAVAGE', 'OFFSET', 'YOUNG THUG', 'TYGA', 'KID INK', 'TINASHE', 'SCHOOLBOY Q', 'KENDRICK LAMAR', 'SIA', 'DAVID GUETTA', 'AKON', 'LIL BOOSIE', 'YUNG JOC', 'BOBBY VALENTINO', 'TIMBALAND', 'KERI HILSON', 'NAS', 'MISSY "MISDEMEANOR" ELLIOTT', 'DA BRAT', 'LIL KIM', 'KEYSHIA COLE', '2PAC', 'SCARFACE', 'JAY Z', 'ANDRE 3000', 'LLOYD', 'YOUNG MONEY', 'GUCCI MANE', 'BIG SEAN'

**Conclusion**

The four questions that started this Billboard charts analysis are answered. The most collaborative Billboard chart musician in the past 50 years is Lil Wayne. The year with the most collaborations is 2017. The artist with the most collaboration in 2017 is Quavo. The longest chain in the collaborations graph has 77 nodes. Some of these findings may seem sensible, like the year with most collaborations and Quavo's collaborations, for people who listen to pop music. However, it may not be so obvious that Lil Wayne is the most collaborative artist, given he has not been much active in recent years. When we looked at the longest chain in the collaborations graph there are some interesting information like Michael Jackson is 10 nodes away from the new hit female rapper Cardi B. There are a lot of interesting information in the collaborations graph and data. Future work includes asking more questions about the data for more analysis.
