Taretto Complete Tutorial
=========================

This guide is designed to show you how to construct and build a testing framework around Taretto.
The beginning assumes you have only done minimal work on your current testing framework and are
starting it from scratch. This does not mean that this is the only way to use Taretto. There are
plenty of opportunities for Taretto to fit into an existing framework, you may like to browse the
various guides and tutorials to see how Taretto can help you out in these cases.

Taretto, like many other systems has an optimal design pattern to follow. Whilst many of the tools
can be utilized in alternative configurations and designs, it is important to know that the best
integrations will be obtained by designing your framework around these fundamental principles.

Taretto Guiding Principles
--------------------------

No one likes reading a ton of documentation, so we'll try to keep this short, however, these
guidelines here represent over 4 years of getting things wrong, trying again and finding an optimal
solution. It should be noted also that these are the collective guidelines of a team of around 10
automation engineers.

We are going to assume we will be testing a simple poll web application, that provides a web
interface, and a REST API. We'll assume that we have a database backend modeling users, polls,
and votes.

* **Polls** - We will have a page that shows a **list** of the *polls* that a user administrates,
  a **details** page for each *poll* showing the *votes* and a page to **add** a new *poll*.
* **Votes** - We will have the page to allow a *vote* to be **cast** on a particular poll. A *user*
  can also see all the *votes* they have cast.
* **Users** - We will have a mechanism for a *user* to **edit** their details and a superuser who
  can **administrate** all of the polls and votes.

