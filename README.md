# dmdma - Dirty Master Data Management Application

A 'dirty' but practical (with a scalable architecture) approach for **Master Data Management** or **Data Warehouse Management**, intended to be flexible and light. The goal is to enabling people who primarily work with data to quickly develop interfaces to their data & Data Warehouse.

This is the "Swiss Army Knife" to quickly develop centralised tools to fill gaps in a data infrastructure (from administration to light reporting), all bespoke to an organisation, or teams requirements.

Based on a simple [Flask](https://palletsprojects.com/p/flask/) Web Application (much of the core functionality/layout is based on the [tutorial](https://flask.palletsprojects.com/en/2.1.x/tutorial/)). It requires no extra client installation/configuration for business users to access (outside of configuring user access). All you need is a simple web server which supports Flask (most of them do with some simple configuration, see the Flask documentation on [Deploying to Production](https://flask.palletsprojects.com/en/2.1.x/deploying/))

Being python based, it can work with *almost* any database, leverage any python libraries/functionality and link to/integrate with many other web frameworks/tools.

Functionality Included (in the examples):

1. Basic authentication (this will need customising for your internal needs), right now it's a (deliberately) placeholder piece of code lifted from the Flask tutorial.
2. Reporting: Displaying results of an SQL Query, allowing them to be downloaded as CSV or browsed using a pivot table (third party javascript library).

Functionality it could include (on my to do list to add examples):

1. User management (including interfacing with third party authentication systems and internal access rights).
2. Reporting on Data Quality issues such as missing mappings.
3. An interface to enable uploading of CSV data (with simple checks on values including date formats) for later consumption by a data process.
4. An interface to fix mapping issues (such as finding references between two datasets and pushing a mapping reference back to a linking table in a data warehouse).
5. Anything which python/flask or connected applications can do

## What this is, and what this isn't

This *is* a framework/example piece, intended for data professionals and teams to quickly build simple bespoke interfaces to their data warehouse (and whatever other infrastructure/applications/tools they wish to incorporate). This is the "Swiss Army Knife" that I've wanted (or been involved in creating parts of) in numerous projects over the years.

This *isn't* intended to be a full "self service" application for data teams to install, configure and hand over to users. It will require work on the part of the team to customise it (at a code level) for their specific needs.

This *isn't* many of the things that it contains (or will contain), for example there is reporting functionality but I wouldn't recommend using this as the base for a reporting tool/platform. It could be done, but for most people/organisations using a bespoke tool like [metabase](https://www.metabase.com/start/oss/) (Has OSS and paid for versions) will be much quicker and easier.

This *is* as quick and dirty way to fill small gaps in the infrastructure of a data team, or an organisations data infrastructure. For example, the reporting functionality allows for custom SQL to be run against a data warehouse (or any database), return results (in a handy object in python) which can be interacted with in python or just thrown onto the webpage (with a download as CSV button).

## Inspiration

After working with data and data teams for many years, I find we are often caught between the development cycles and goals of other parts of the business, and while we often have many tools to do our jobs.

## Design & Architecture Decisions

I've chosen to use python as that's the common language that most people working with data pick up, it's also the language (mostly the [jinja](https://palletsprojects.com/p/jinja/) templating part) that's leveraged by [DBT](https://www.getdbt.com/) (Data Build Tool). This way it's something that's going to be familiar to most data engineers and analysts.

## Leveraged Technologies

While python/Flask sit at the core of this (if you wish to switch from one of those, this project probably isn't the best starting place). Most other tools/libraries are optional and interchangeable down to personal preference/needs.

 - [Bootstrap](https://getbootstrap.com/) - Embedded in the templates to create responsive and more attractive.
 - [SQLite](https://www.sqlite.org/index.html) - implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. Most cases where this is used for examples, it's best to replace with links to your actual database.
 - [pandas](https://pandas.pydata.org/) - pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.

# Installation & Configuration

Most of this is covered under Flask and related documentation.

## Using this for your own project

If you want to build your own implementation using this as a base, either form the project or just copy out the files. Because of the template nature of this project and idea for each solution to be bespoke to its needs, checking out the codebase directly and working on it probably isn't the best plan of action.

## Contributing your own Examples

If you have a use-case which can be added as an example, I'd love to see it. I'm sharing my ideas in the hope that there is something here which inspires others who work with data to create solutions to common problems. If you have a solution I'd love to se it as I'm always trying to solve problems.

# Further Documentation

 - [Flask](https://flask.palletsprojects.com/) - The core 'mini' web application framework
 - [Bootstrap](https://getbootstrap.com/) - The "Powerful, extensible, and feature-packed frontend toolkit", used to create responsive pages and a consistent look with minimal development effort.
