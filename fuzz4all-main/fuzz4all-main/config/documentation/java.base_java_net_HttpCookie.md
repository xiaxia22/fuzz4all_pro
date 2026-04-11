# Class HttpCookie

**Source:** `java.base\java\net\HttpCookie.html`

### Class Description

```java
public final class
HttpCookie

extends
Object

implements
Cloneable
```

An HttpCookie object represents an HTTP cookie, which carries state
information between server and user agent. Cookie is widely adopted
to create stateful sessions.

There are 3 HTTP cookie specifications:

Netscape draft

RFC 2109 -

http://www.ietf.org/rfc/rfc2109.txt

RFC 2965 -

http://www.ietf.org/rfc/rfc2965.txt

HttpCookie class can accept all these 3 forms of syntax.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public HttpCookie​(
String
name,

String
value)

Constructs a cookie with a specified name and value.

The name must conform to RFC 2965. That means it can contain
only ASCII alphanumeric characters and cannot contain commas,
semicolons, or white space or begin with a $ character. The cookie's
name cannot be changed after creation.

The value can be anything the server chooses to send. Its
value is probably of interest only to the server. The cookie's
value can be changed after creation with the

setValue

method.

By default, cookies are created according to the RFC 2965
cookie specification. The version can be changed with the

setVersion

method.

**Parameters:**
- name

- a

String

specifying the name of the cookie
- value

- a

String

specifying the value of the cookie

**Throws:**
- IllegalArgumentException

- if the cookie name contains illegal characters
- NullPointerException

- if

name

is

null

**See Also:**
- setValue(java.lang.String)

,

setVersion(int)

---

### Method Details

#### public static
List
<
HttpCookie
> parse​(
String
header)

Constructs cookies from set-cookie or set-cookie2 header string.
RFC 2965 section 3.2.2 set-cookie2 syntax indicates that one header line
may contain more than one cookie definitions, so this is a static
utility method instead of another constructor.

**Parameters:**
- header

- a

String

specifying the set-cookie header. The header
should start with "set-cookie", or "set-cookie2" token; or it
should have no leading token at all.

**Returns:**
- a List of cookie parsed from header line string

**Throws:**
- IllegalArgumentException

- if header string violates the cookie specification's syntax or
the cookie name contains illegal characters.
- NullPointerException

- if the header string is

null

---

#### public boolean hasExpired()

Reports whether this HTTP cookie has expired or not.

**Returns:**
- true

to indicate this HTTP cookie has expired;
otherwise,

false

---

#### public void setComment​(
String
purpose)

Specifies a comment that describes a cookie's purpose.
The comment is useful if the browser presents the cookie
to the user. Comments are not supported by Netscape Version 0 cookies.

**Parameters:**
- purpose

- a

String

specifying the comment to display to the user

**See Also:**
- getComment()

---

#### public
String
getComment()

Returns the comment describing the purpose of this cookie, or

null

if the cookie has no comment.

**Returns:**
- a

String

containing the comment, or

null

if none

**See Also:**
- setComment(java.lang.String)

---

#### public void setCommentURL​(
String
purpose)

Specifies a comment URL that describes a cookie's purpose.
The comment URL is useful if the browser presents the cookie
to the user. Comment URL is RFC 2965 only.

**Parameters:**
- purpose

- a

String

specifying the comment URL to display to the user

**See Also:**
- getCommentURL()

---

#### public
String
getCommentURL()

Returns the comment URL describing the purpose of this cookie, or

null

if the cookie has no comment URL.

**Returns:**
- a

String

containing the comment URL, or

null

if none

**See Also:**
- setCommentURL(java.lang.String)

---

#### public void setDiscard​(boolean discard)

Specify whether user agent should discard the cookie unconditionally.
This is RFC 2965 only attribute.

**Parameters:**
- discard

-

true

indicates to discard cookie unconditionally

**See Also:**
- getDiscard()

---

#### public boolean getDiscard()

Returns the discard attribute of the cookie

**Returns:**
- a

boolean

to represent this cookie's discard attribute

**See Also:**
- setDiscard(boolean)

---

#### public void setPortlist​(
String
ports)

Specify the portlist of the cookie, which restricts the port(s)
to which a cookie may be sent back in a Cookie header.

**Parameters:**
- ports

- a

String

specify the port list, which is comma separated
series of digits

**See Also:**
- getPortlist()

---

#### public
String
getPortlist()

Returns the port list attribute of the cookie

**Returns:**
- a

String

contains the port list or

null

if none

**See Also:**
- setPortlist(java.lang.String)

---

#### public void setDomain​(
String
pattern)

Specifies the domain within which this cookie should be presented.

The form of the domain name is specified by RFC 2965. A domain
name begins with a dot (

.foo.com

) and means that
the cookie is visible to servers in a specified Domain Name System
(DNS) zone (for example,

www.foo.com

, but not

a.b.foo.com

). By default, cookies are only returned
to the server that sent them.

**Parameters:**
- pattern

- a

String

containing the domain name within which this
cookie is visible; form is according to RFC 2965

**See Also:**
- getDomain()

---

#### public
String
getDomain()

Returns the domain name set for this cookie. The form of the domain name
is set by RFC 2965.

**Returns:**
- a

String

containing the domain name

**See Also:**
- setDomain(java.lang.String)

---

#### public void setMaxAge​(long expiry)

Sets the maximum age of the cookie in seconds.

A positive value indicates that the cookie will expire
after that many seconds have passed. Note that the value is
the

maximum

age when the cookie will expire, not the cookie's
current age.

A negative value means that the cookie is not stored persistently
and will be deleted when the Web browser exits. A zero value causes the
cookie to be deleted.

**Parameters:**
- expiry

- an integer specifying the maximum age of the cookie in seconds;
if zero, the cookie should be discarded immediately; otherwise,
the cookie's max age is unspecified.

**See Also:**
- getMaxAge()

---

#### public long getMaxAge()

Returns the maximum age of the cookie, specified in seconds. By default,

-1

indicating the cookie will persist until browser shutdown.

**Returns:**
- an integer specifying the maximum age of the cookie in seconds

**See Also:**
- setMaxAge(long)

---

#### public void setPath​(
String
uri)

Specifies a path for the cookie to which the client should return
the cookie.

The cookie is visible to all the pages in the directory
you specify, and all the pages in that directory's subdirectories.
A cookie's path must include the servlet that set the cookie,
for example,

/catalog

, which makes the cookie
visible to all directories on the server under

/catalog

.

Consult RFC 2965 (available on the Internet) for more
information on setting path names for cookies.

**Parameters:**
- uri

- a

String

specifying a path

**See Also:**
- getPath()

---

#### public
String
getPath()

Returns the path on the server to which the browser returns this cookie.
The cookie is visible to all subpaths on the server.

**Returns:**
- a

String

specifying a path that contains a servlet name,
for example,

/catalog

**See Also:**
- setPath(java.lang.String)

---

#### public void setSecure​(boolean flag)

Indicates whether the cookie should only be sent using a secure protocol,
such as HTTPS or SSL.

The default value is

false

.

**Parameters:**
- flag

- If

true

, the cookie can only be sent over a secure
protocol like HTTPS. If

false

, it can be sent over
any protocol.

**See Also:**
- getSecure()

---

#### public boolean getSecure()

Returns

true

if sending this cookie should be restricted to a
secure protocol, or

false

if the it can be sent using any
protocol.

**Returns:**
- false

if the cookie can be sent over any standard
protocol; otherwise,

true

**See Also:**
- setSecure(boolean)

---

#### public
String
getName()

Returns the name of the cookie. The name cannot be changed after
creation.

**Returns:**
- a

String

specifying the cookie's name

---

#### public void setValue​(
String
newValue)

Assigns a new value to a cookie after the cookie is created.
If you use a binary value, you may want to use BASE64 encoding.

With Version 0 cookies, values should not contain white space,
brackets, parentheses, equals signs, commas, double quotes, slashes,
question marks, at signs, colons, and semicolons. Empty values may not
behave the same way on all browsers.

**Parameters:**
- newValue

- a

String

specifying the new value

**See Also:**
- getValue()

---

#### public
String
getValue()

Returns the value of the cookie.

**Returns:**
- a

String

containing the cookie's present value

**See Also:**
- setValue(java.lang.String)

---

#### public int getVersion()

Returns the version of the protocol this cookie complies with. Version 1
complies with RFC 2965/2109, and version 0 complies with the original
cookie specification drafted by Netscape. Cookies provided by a browser
use and identify the browser's cookie version.

**Returns:**
- 0 if the cookie complies with the original Netscape
specification; 1 if the cookie complies with RFC 2965/2109

**See Also:**
- setVersion(int)

---

#### public void setVersion​(int v)

Sets the version of the cookie protocol this cookie complies
with. Version 0 complies with the original Netscape cookie
specification. Version 1 complies with RFC 2965/2109.

**Parameters:**
- v

- 0 if the cookie should comply with the original Netscape
specification; 1 if the cookie should comply with RFC 2965/2109

**Throws:**
- IllegalArgumentException

- if

v

is neither 0 nor 1

**See Also:**
- getVersion()

---

#### public boolean isHttpOnly()

Returns

true

if this cookie contains the

HttpOnly

attribute. This means that the cookie should not be accessible to
scripting engines, like javascript.

**Returns:**
- true

if this cookie should be considered HTTPOnly

**See Also:**
- setHttpOnly(boolean)

---

#### public void setHttpOnly​(boolean httpOnly)

Indicates whether the cookie should be considered HTTP Only. If set to

true

it means the cookie should not be accessible to scripting
engines like javascript.

**Parameters:**
- httpOnly

- if

true

make the cookie HTTP only, i.e. only visible as
part of an HTTP request.

**See Also:**
- isHttpOnly()

---

#### public static boolean domainMatches​(
String
domain,

String
host)

The utility method to check whether a host name is in a domain or not.

This concept is described in the cookie specification.
To understand the concept, some terminologies need to be defined first:

effective host name = hostname if host name contains dot

or = hostname.local if not

Host A's name domain-matches host B's if:

- their host name strings string-compare equal; or
- A is a HDN string and has the form NB, where N is a non-empty
name string, B has the form .B', and B' is a HDN string. (So,
x.y.com domain-matches .Y.com but not Y.com.)

A host isn't in a domain (RFC 2965 sec. 3.3.2) if:

- The value for the Domain attribute contains no embedded dots,
and the value is not .local.
- The effective host name that derives from the request-host does
not domain-match the Domain attribute.
- The request-host is a HDN (not IP address) and has the form HD,
where D is the value of the Domain attribute, and H is a string
that contains one or more dots.

Examples:

- A Set-Cookie2 from request-host y.x.foo.com for Domain=.foo.com
would be rejected, because H is y.x and contains a dot.
- A Set-Cookie2 from request-host x.foo.com for Domain=.foo.com
would be accepted.
- A Set-Cookie2 with Domain=.com or Domain=.com., will always be
rejected, because there is no embedded dot.
- A Set-Cookie2 from request-host example for Domain=.local will
be accepted, because the effective host name for the request-
host is example.local, and example.local domain-matches .local.

**Parameters:**
- domain

- the domain name to check host name with
- host

- the host name in question

**Returns:**
- true

if they domain-matches;

false

if not

---

#### public
String
toString()

Constructs a cookie header string representation of this cookie,
which is in the format defined by corresponding cookie specification,
but without the leading "Cookie:" token.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string form of the cookie. The string has the defined format

---

#### public boolean equals​(
Object
obj)

Test the equality of two HTTP cookies.

The result is

true

only if two cookies come from same domain
(case-insensitive), have same name (case-insensitive), and have same path
(case-sensitive).

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if two HTTP cookies equal to each other;
otherwise,

false

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code of this HTTP cookie. The result is the sum of
hash code value of three significant components of this cookie: name,
domain, and path. That is, the hash code is the value of the expression:

getName().toLowerCase().hashCode()

+ getDomain().toLowerCase().hashCode()

+ getPath().hashCode()

**Overrides:**
- hashCode

in class

Object

**Returns:**
- this HTTP cookie's hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
Object
clone()

Create and return a copy of this object.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this HTTP cookie

**See Also:**
- Cloneable

---

### Additional Sections

#### Class HttpCookie

java.lang.Object

- java.net.HttpCookie

java.net.HttpCookie

**All Implemented Interfaces:** Cloneable

```java
public final class
HttpCookie

extends
Object

implements
Cloneable
```

An HttpCookie object represents an HTTP cookie, which carries state
information between server and user agent. Cookie is widely adopted
to create stateful sessions.

There are 3 HTTP cookie specifications:

Netscape draft

RFC 2109 -

http://www.ietf.org/rfc/rfc2109.txt

RFC 2965 -

http://www.ietf.org/rfc/rfc2965.txt

HttpCookie class can accept all these 3 forms of syntax.

**Since:** 1.6

public final class

HttpCookie

extends

Object

implements

Cloneable

An HttpCookie object represents an HTTP cookie, which carries state
information between server and user agent. Cookie is widely adopted
to create stateful sessions.

There are 3 HTTP cookie specifications:

Netscape draft

RFC 2109 -

http://www.ietf.org/rfc/rfc2109.txt

RFC 2965 -

http://www.ietf.org/rfc/rfc2965.txt

HttpCookie class can accept all these 3 forms of syntax.

There are 3 HTTP cookie specifications:

Netscape draft

RFC 2109 -

http://www.ietf.org/rfc/rfc2109.txt

RFC 2965 -

http://www.ietf.org/rfc/rfc2965.txt

HttpCookie class can accept all these 3 forms of syntax.

HttpCookie class can accept all these 3 forms of syntax.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HttpCookie

​(

String

name,

String

value)

Constructs a cookie with a specified name and value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Create and return a copy of this object.

static boolean

domainMatches

​(

String

domain,

String

host)

The utility method to check whether a host name is in a domain or not.

boolean

equals

​(

Object

obj)

Test the equality of two HTTP cookies.

String

getComment

()

Returns the comment describing the purpose of this cookie, or

null

if the cookie has no comment.

String

getCommentURL

()

Returns the comment URL describing the purpose of this cookie, or

null

if the cookie has no comment URL.

boolean

getDiscard

()

Returns the discard attribute of the cookie

String

getDomain

()

Returns the domain name set for this cookie.

long

getMaxAge

()

Returns the maximum age of the cookie, specified in seconds.

String

getName

()

Returns the name of the cookie.

String

getPath

()

Returns the path on the server to which the browser returns this cookie.

String

getPortlist

()

Returns the port list attribute of the cookie

boolean

getSecure

()

Returns

true

if sending this cookie should be restricted to a
secure protocol, or

false

if the it can be sent using any
protocol.

String

getValue

()

Returns the value of the cookie.

int

getVersion

()

Returns the version of the protocol this cookie complies with.

boolean

hasExpired

()

Reports whether this HTTP cookie has expired or not.

int

hashCode

()

Returns the hash code of this HTTP cookie.

boolean

isHttpOnly

()

Returns

true

if this cookie contains the

HttpOnly

attribute.

static

List

<

HttpCookie

>

parse

​(

String

header)

Constructs cookies from set-cookie or set-cookie2 header string.

void

setComment

​(

String

purpose)

Specifies a comment that describes a cookie's purpose.

void

setCommentURL

​(

String

purpose)

Specifies a comment URL that describes a cookie's purpose.

void

setDiscard

​(boolean discard)

Specify whether user agent should discard the cookie unconditionally.

void

setDomain

​(

String

pattern)

Specifies the domain within which this cookie should be presented.

void

setHttpOnly

​(boolean httpOnly)

Indicates whether the cookie should be considered HTTP Only.

void

setMaxAge

​(long expiry)

Sets the maximum age of the cookie in seconds.

void

setPath

​(

String

uri)

Specifies a path for the cookie to which the client should return
the cookie.

void

setPortlist

​(

String

ports)

Specify the portlist of the cookie, which restricts the port(s)
to which a cookie may be sent back in a Cookie header.

void

setSecure

​(boolean flag)

Indicates whether the cookie should only be sent using a secure protocol,
such as HTTPS or SSL.

void

setValue

​(

String

newValue)

Assigns a new value to a cookie after the cookie is created.

void

setVersion

​(int v)

Sets the version of the cookie protocol this cookie complies
with.

String

toString

()

Constructs a cookie header string representation of this cookie,
which is in the format defined by corresponding cookie specification,
but without the leading "Cookie:" token.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

HttpCookie

​(

String

name,

String

value)

Constructs a cookie with a specified name and value.

---

#### Constructor Summary

Constructs a cookie with a specified name and value.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Create and return a copy of this object.

static boolean

domainMatches

​(

String

domain,

String

host)

The utility method to check whether a host name is in a domain or not.

boolean

equals

​(

Object

obj)

Test the equality of two HTTP cookies.

String

getComment

()

Returns the comment describing the purpose of this cookie, or

null

if the cookie has no comment.

String

getCommentURL

()

Returns the comment URL describing the purpose of this cookie, or

null

if the cookie has no comment URL.

boolean

getDiscard

()

Returns the discard attribute of the cookie

String

getDomain

()

Returns the domain name set for this cookie.

long

getMaxAge

()

Returns the maximum age of the cookie, specified in seconds.

String

getName

()

Returns the name of the cookie.

String

getPath

()

Returns the path on the server to which the browser returns this cookie.

String

getPortlist

()

Returns the port list attribute of the cookie

boolean

getSecure

()

Returns

true

if sending this cookie should be restricted to a
secure protocol, or

false

if the it can be sent using any
protocol.

String

getValue

()

Returns the value of the cookie.

int

getVersion

()

Returns the version of the protocol this cookie complies with.

boolean

hasExpired

()

Reports whether this HTTP cookie has expired or not.

int

hashCode

()

Returns the hash code of this HTTP cookie.

boolean

isHttpOnly

()

Returns

true

if this cookie contains the

HttpOnly

attribute.

static

List

<

HttpCookie

>

parse

​(

String

header)

Constructs cookies from set-cookie or set-cookie2 header string.

void

setComment

​(

String

purpose)

Specifies a comment that describes a cookie's purpose.

void

setCommentURL

​(

String

purpose)

Specifies a comment URL that describes a cookie's purpose.

void

setDiscard

​(boolean discard)

Specify whether user agent should discard the cookie unconditionally.

void

setDomain

​(

String

pattern)

Specifies the domain within which this cookie should be presented.

void

setHttpOnly

​(boolean httpOnly)

Indicates whether the cookie should be considered HTTP Only.

void

setMaxAge

​(long expiry)

Sets the maximum age of the cookie in seconds.

void

setPath

​(

String

uri)

Specifies a path for the cookie to which the client should return
the cookie.

void

setPortlist

​(

String

ports)

Specify the portlist of the cookie, which restricts the port(s)
to which a cookie may be sent back in a Cookie header.

void

setSecure

​(boolean flag)

Indicates whether the cookie should only be sent using a secure protocol,
such as HTTPS or SSL.

void

setValue

​(

String

newValue)

Assigns a new value to a cookie after the cookie is created.

void

setVersion

​(int v)

Sets the version of the cookie protocol this cookie complies
with.

String

toString

()

Constructs a cookie header string representation of this cookie,
which is in the format defined by corresponding cookie specification,
but without the leading "Cookie:" token.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Create and return a copy of this object.

The utility method to check whether a host name is in a domain or not.

Test the equality of two HTTP cookies.

Returns the comment describing the purpose of this cookie, or

null

if the cookie has no comment.

Returns the comment URL describing the purpose of this cookie, or

null

if the cookie has no comment URL.

Returns the discard attribute of the cookie

Returns the domain name set for this cookie.

Returns the maximum age of the cookie, specified in seconds.

Returns the name of the cookie.

Returns the path on the server to which the browser returns this cookie.

Returns the port list attribute of the cookie

Returns

true

if sending this cookie should be restricted to a
secure protocol, or

false

if the it can be sent using any
protocol.

Returns the value of the cookie.

Returns the version of the protocol this cookie complies with.

Reports whether this HTTP cookie has expired or not.

Returns the hash code of this HTTP cookie.

Returns

true

if this cookie contains the

HttpOnly

attribute.

Constructs cookies from set-cookie or set-cookie2 header string.

Specifies a comment that describes a cookie's purpose.

Specifies a comment URL that describes a cookie's purpose.

Specify whether user agent should discard the cookie unconditionally.

Specifies the domain within which this cookie should be presented.

Indicates whether the cookie should be considered HTTP Only.

Sets the maximum age of the cookie in seconds.

Specifies a path for the cookie to which the client should return
the cookie.

Specify the portlist of the cookie, which restricts the port(s)
to which a cookie may be sent back in a Cookie header.

Indicates whether the cookie should only be sent using a secure protocol,
such as HTTPS or SSL.

Assigns a new value to a cookie after the cookie is created.

Sets the version of the cookie protocol this cookie complies
with.

Constructs a cookie header string representation of this cookie,
which is in the format defined by corresponding cookie specification,
but without the leading "Cookie:" token.

Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HttpCookie

```java
public HttpCookie​(
String
name,

String
value)
```

Constructs a cookie with a specified name and value.

The name must conform to RFC 2965. That means it can contain
only ASCII alphanumeric characters and cannot contain commas,
semicolons, or white space or begin with a $ character. The cookie's
name cannot be changed after creation.

The value can be anything the server chooses to send. Its
value is probably of interest only to the server. The cookie's
value can be changed after creation with the

setValue

method.

By default, cookies are created according to the RFC 2965
cookie specification. The version can be changed with the

setVersion

method.

**Parameters:** name

- a

String

specifying the name of the cookie
**Parameters:** value

- a

String

specifying the value of the cookie
**Throws:** IllegalArgumentException

- if the cookie name contains illegal characters
**Throws:** NullPointerException

- if

name

is

null
**See Also:** setValue(java.lang.String)

,

setVersion(int)

============ METHOD DETAIL ==========

- Method Detail

- parse

```java
public static
List
<
HttpCookie
> parse​(
String
header)
```

Constructs cookies from set-cookie or set-cookie2 header string.
RFC 2965 section 3.2.2 set-cookie2 syntax indicates that one header line
may contain more than one cookie definitions, so this is a static
utility method instead of another constructor.

**Parameters:** header

- a

String

specifying the set-cookie header. The header
should start with "set-cookie", or "set-cookie2" token; or it
should have no leading token at all.
**Returns:** a List of cookie parsed from header line string
**Throws:** IllegalArgumentException

- if header string violates the cookie specification's syntax or
the cookie name contains illegal characters.
**Throws:** NullPointerException

- if the header string is

null

- hasExpired

```java
public boolean hasExpired()
```

Reports whether this HTTP cookie has expired or not.

**Returns:** true

to indicate this HTTP cookie has expired;
otherwise,

false

- setComment

```java
public void setComment​(
String
purpose)
```

Specifies a comment that describes a cookie's purpose.
The comment is useful if the browser presents the cookie
to the user. Comments are not supported by Netscape Version 0 cookies.

**Parameters:** purpose

- a

String

specifying the comment to display to the user
**See Also:** getComment()

- getComment

```java
public
String
getComment()
```

Returns the comment describing the purpose of this cookie, or

null

if the cookie has no comment.

**Returns:** a

String

containing the comment, or

null

if none
**See Also:** setComment(java.lang.String)

- setCommentURL

```java
public void setCommentURL​(
String
purpose)
```

Specifies a comment URL that describes a cookie's purpose.
The comment URL is useful if the browser presents the cookie
to the user. Comment URL is RFC 2965 only.

**Parameters:** purpose

- a

String

specifying the comment URL to display to the user
**See Also:** getCommentURL()

- getCommentURL

```java
public
String
getCommentURL()
```

Returns the comment URL describing the purpose of this cookie, or

null

if the cookie has no comment URL.

**Returns:** a

String

containing the comment URL, or

null

if none
**See Also:** setCommentURL(java.lang.String)

- setDiscard

```java
public void setDiscard​(boolean discard)
```

Specify whether user agent should discard the cookie unconditionally.
This is RFC 2965 only attribute.

**Parameters:** discard

-

true

indicates to discard cookie unconditionally
**See Also:** getDiscard()

- getDiscard

```java
public boolean getDiscard()
```

Returns the discard attribute of the cookie

**Returns:** a

boolean

to represent this cookie's discard attribute
**See Also:** setDiscard(boolean)

- setPortlist

```java
public void setPortlist​(
String
ports)
```

Specify the portlist of the cookie, which restricts the port(s)
to which a cookie may be sent back in a Cookie header.

**Parameters:** ports

- a

String

specify the port list, which is comma separated
series of digits
**See Also:** getPortlist()

- getPortlist

```java
public
String
getPortlist()
```

Returns the port list attribute of the cookie

**Returns:** a

String

contains the port list or

null

if none
**See Also:** setPortlist(java.lang.String)

- setDomain

```java
public void setDomain​(
String
pattern)
```

Specifies the domain within which this cookie should be presented.

The form of the domain name is specified by RFC 2965. A domain
name begins with a dot (

.foo.com

) and means that
the cookie is visible to servers in a specified Domain Name System
(DNS) zone (for example,

www.foo.com

, but not

a.b.foo.com

). By default, cookies are only returned
to the server that sent them.

**Parameters:** pattern

- a

String

containing the domain name within which this
cookie is visible; form is according to RFC 2965
**See Also:** getDomain()

- getDomain

```java
public
String
getDomain()
```

Returns the domain name set for this cookie. The form of the domain name
is set by RFC 2965.

**Returns:** a

String

containing the domain name
**See Also:** setDomain(java.lang.String)

- setMaxAge

```java
public void setMaxAge​(long expiry)
```

Sets the maximum age of the cookie in seconds.

A positive value indicates that the cookie will expire
after that many seconds have passed. Note that the value is
the

maximum

age when the cookie will expire, not the cookie's
current age.

A negative value means that the cookie is not stored persistently
and will be deleted when the Web browser exits. A zero value causes the
cookie to be deleted.

**Parameters:** expiry

- an integer specifying the maximum age of the cookie in seconds;
if zero, the cookie should be discarded immediately; otherwise,
the cookie's max age is unspecified.
**See Also:** getMaxAge()

- getMaxAge

```java
public long getMaxAge()
```

Returns the maximum age of the cookie, specified in seconds. By default,

-1

indicating the cookie will persist until browser shutdown.

**Returns:** an integer specifying the maximum age of the cookie in seconds
**See Also:** setMaxAge(long)

- setPath

```java
public void setPath​(
String
uri)
```

Specifies a path for the cookie to which the client should return
the cookie.

The cookie is visible to all the pages in the directory
you specify, and all the pages in that directory's subdirectories.
A cookie's path must include the servlet that set the cookie,
for example,

/catalog

, which makes the cookie
visible to all directories on the server under

/catalog

.

Consult RFC 2965 (available on the Internet) for more
information on setting path names for cookies.

**Parameters:** uri

- a

String

specifying a path
**See Also:** getPath()

- getPath

```java
public
String
getPath()
```

Returns the path on the server to which the browser returns this cookie.
The cookie is visible to all subpaths on the server.

**Returns:** a

String

specifying a path that contains a servlet name,
for example,

/catalog
**See Also:** setPath(java.lang.String)

- setSecure

```java
public void setSecure​(boolean flag)
```

Indicates whether the cookie should only be sent using a secure protocol,
such as HTTPS or SSL.

The default value is

false

.

**Parameters:** flag

- If

true

, the cookie can only be sent over a secure
protocol like HTTPS. If

false

, it can be sent over
any protocol.
**See Also:** getSecure()

- getSecure

```java
public boolean getSecure()
```

Returns

true

if sending this cookie should be restricted to a
secure protocol, or

false

if the it can be sent using any
protocol.

**Returns:** false

if the cookie can be sent over any standard
protocol; otherwise,

true
**See Also:** setSecure(boolean)

- getName

```java
public
String
getName()
```

Returns the name of the cookie. The name cannot be changed after
creation.

**Returns:** a

String

specifying the cookie's name

- setValue

```java
public void setValue​(
String
newValue)
```

Assigns a new value to a cookie after the cookie is created.
If you use a binary value, you may want to use BASE64 encoding.

With Version 0 cookies, values should not contain white space,
brackets, parentheses, equals signs, commas, double quotes, slashes,
question marks, at signs, colons, and semicolons. Empty values may not
behave the same way on all browsers.

**Parameters:** newValue

- a

String

specifying the new value
**See Also:** getValue()

- getValue

```java
public
String
getValue()
```

Returns the value of the cookie.

**Returns:** a

String

containing the cookie's present value
**See Also:** setValue(java.lang.String)

- getVersion

```java
public int getVersion()
```

Returns the version of the protocol this cookie complies with. Version 1
complies with RFC 2965/2109, and version 0 complies with the original
cookie specification drafted by Netscape. Cookies provided by a browser
use and identify the browser's cookie version.

**Returns:** 0 if the cookie complies with the original Netscape
specification; 1 if the cookie complies with RFC 2965/2109
**See Also:** setVersion(int)

- setVersion

```java
public void setVersion​(int v)
```

Sets the version of the cookie protocol this cookie complies
with. Version 0 complies with the original Netscape cookie
specification. Version 1 complies with RFC 2965/2109.

**Parameters:** v

- 0 if the cookie should comply with the original Netscape
specification; 1 if the cookie should comply with RFC 2965/2109
**Throws:** IllegalArgumentException

- if

v

is neither 0 nor 1
**See Also:** getVersion()

- isHttpOnly

```java
public boolean isHttpOnly()
```

Returns

true

if this cookie contains the

HttpOnly

attribute. This means that the cookie should not be accessible to
scripting engines, like javascript.

**Returns:** true

if this cookie should be considered HTTPOnly
**See Also:** setHttpOnly(boolean)

- setHttpOnly

```java
public void setHttpOnly​(boolean httpOnly)
```

Indicates whether the cookie should be considered HTTP Only. If set to

true

it means the cookie should not be accessible to scripting
engines like javascript.

**Parameters:** httpOnly

- if

true

make the cookie HTTP only, i.e. only visible as
part of an HTTP request.
**See Also:** isHttpOnly()

- domainMatches

```java
public static boolean domainMatches​(
String
domain,

String
host)
```

The utility method to check whether a host name is in a domain or not.

This concept is described in the cookie specification.
To understand the concept, some terminologies need to be defined first:

effective host name = hostname if host name contains dot

or = hostname.local if not

Host A's name domain-matches host B's if:

- their host name strings string-compare equal; or
- A is a HDN string and has the form NB, where N is a non-empty
name string, B has the form .B', and B' is a HDN string. (So,
x.y.com domain-matches .Y.com but not Y.com.)

A host isn't in a domain (RFC 2965 sec. 3.3.2) if:

- The value for the Domain attribute contains no embedded dots,
and the value is not .local.
- The effective host name that derives from the request-host does
not domain-match the Domain attribute.
- The request-host is a HDN (not IP address) and has the form HD,
where D is the value of the Domain attribute, and H is a string
that contains one or more dots.

Examples:

- A Set-Cookie2 from request-host y.x.foo.com for Domain=.foo.com
would be rejected, because H is y.x and contains a dot.
- A Set-Cookie2 from request-host x.foo.com for Domain=.foo.com
would be accepted.
- A Set-Cookie2 with Domain=.com or Domain=.com., will always be
rejected, because there is no embedded dot.
- A Set-Cookie2 from request-host example for Domain=.local will
be accepted, because the effective host name for the request-
host is example.local, and example.local domain-matches .local.

**Parameters:** domain

- the domain name to check host name with
**Parameters:** host

- the host name in question
**Returns:** true

if they domain-matches;

false

if not

- toString

```java
public
String
toString()
```

Constructs a cookie header string representation of this cookie,
which is in the format defined by corresponding cookie specification,
but without the leading "Cookie:" token.

**Overrides:** toString

in class

Object
**Returns:** a string form of the cookie. The string has the defined format

- equals

```java
public boolean equals​(
Object
obj)
```

Test the equality of two HTTP cookies.

The result is

true

only if two cookies come from same domain
(case-insensitive), have same name (case-insensitive), and have same path
(case-sensitive).

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if two HTTP cookies equal to each other;
otherwise,

false
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code of this HTTP cookie. The result is the sum of
hash code value of three significant components of this cookie: name,
domain, and path. That is, the hash code is the value of the expression:

getName().toLowerCase().hashCode()

+ getDomain().toLowerCase().hashCode()

+ getPath().hashCode()

**Overrides:** hashCode

in class

Object
**Returns:** this HTTP cookie's hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Create and return a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this HTTP cookie
**See Also:** Cloneable

Constructor Detail

- HttpCookie

```java
public HttpCookie​(
String
name,

String
value)
```

Constructs a cookie with a specified name and value.

The name must conform to RFC 2965. That means it can contain
only ASCII alphanumeric characters and cannot contain commas,
semicolons, or white space or begin with a $ character. The cookie's
name cannot be changed after creation.

The value can be anything the server chooses to send. Its
value is probably of interest only to the server. The cookie's
value can be changed after creation with the

setValue

method.

By default, cookies are created according to the RFC 2965
cookie specification. The version can be changed with the

setVersion

method.

**Parameters:** name

- a

String

specifying the name of the cookie
**Parameters:** value

- a

String

specifying the value of the cookie
**Throws:** IllegalArgumentException

- if the cookie name contains illegal characters
**Throws:** NullPointerException

- if

name

is

null
**See Also:** setValue(java.lang.String)

,

setVersion(int)

---

#### Constructor Detail

HttpCookie

```java
public HttpCookie​(
String
name,

String
value)
```

Constructs a cookie with a specified name and value.

The name must conform to RFC 2965. That means it can contain
only ASCII alphanumeric characters and cannot contain commas,
semicolons, or white space or begin with a $ character. The cookie's
name cannot be changed after creation.

The value can be anything the server chooses to send. Its
value is probably of interest only to the server. The cookie's
value can be changed after creation with the

setValue

method.

By default, cookies are created according to the RFC 2965
cookie specification. The version can be changed with the

setVersion

method.

**Parameters:** name

- a

String

specifying the name of the cookie
**Parameters:** value

- a

String

specifying the value of the cookie
**Throws:** IllegalArgumentException

- if the cookie name contains illegal characters
**Throws:** NullPointerException

- if

name

is

null
**See Also:** setValue(java.lang.String)

,

setVersion(int)

---

#### HttpCookie

public HttpCookie​(

String

name,

String

value)

Constructs a cookie with a specified name and value.

The name must conform to RFC 2965. That means it can contain
only ASCII alphanumeric characters and cannot contain commas,
semicolons, or white space or begin with a $ character. The cookie's
name cannot be changed after creation.

The value can be anything the server chooses to send. Its
value is probably of interest only to the server. The cookie's
value can be changed after creation with the

setValue

method.

By default, cookies are created according to the RFC 2965
cookie specification. The version can be changed with the

setVersion

method.

The name must conform to RFC 2965. That means it can contain
only ASCII alphanumeric characters and cannot contain commas,
semicolons, or white space or begin with a $ character. The cookie's
name cannot be changed after creation.

The value can be anything the server chooses to send. Its
value is probably of interest only to the server. The cookie's
value can be changed after creation with the

setValue

method.

By default, cookies are created according to the RFC 2965
cookie specification. The version can be changed with the

setVersion

method.

The value can be anything the server chooses to send. Its
value is probably of interest only to the server. The cookie's
value can be changed after creation with the

setValue

method.

By default, cookies are created according to the RFC 2965
cookie specification. The version can be changed with the

setVersion

method.

By default, cookies are created according to the RFC 2965
cookie specification. The version can be changed with the

setVersion

method.

Method Detail

- parse

```java
public static
List
<
HttpCookie
> parse​(
String
header)
```

Constructs cookies from set-cookie or set-cookie2 header string.
RFC 2965 section 3.2.2 set-cookie2 syntax indicates that one header line
may contain more than one cookie definitions, so this is a static
utility method instead of another constructor.

**Parameters:** header

- a

String

specifying the set-cookie header. The header
should start with "set-cookie", or "set-cookie2" token; or it
should have no leading token at all.
**Returns:** a List of cookie parsed from header line string
**Throws:** IllegalArgumentException

- if header string violates the cookie specification's syntax or
the cookie name contains illegal characters.
**Throws:** NullPointerException

- if the header string is

null

- hasExpired

```java
public boolean hasExpired()
```

Reports whether this HTTP cookie has expired or not.

**Returns:** true

to indicate this HTTP cookie has expired;
otherwise,

false

- setComment

```java
public void setComment​(
String
purpose)
```

Specifies a comment that describes a cookie's purpose.
The comment is useful if the browser presents the cookie
to the user. Comments are not supported by Netscape Version 0 cookies.

**Parameters:** purpose

- a

String

specifying the comment to display to the user
**See Also:** getComment()

- getComment

```java
public
String
getComment()
```

Returns the comment describing the purpose of this cookie, or

null

if the cookie has no comment.

**Returns:** a

String

containing the comment, or

null

if none
**See Also:** setComment(java.lang.String)

- setCommentURL

```java
public void setCommentURL​(
String
purpose)
```

Specifies a comment URL that describes a cookie's purpose.
The comment URL is useful if the browser presents the cookie
to the user. Comment URL is RFC 2965 only.

**Parameters:** purpose

- a

String

specifying the comment URL to display to the user
**See Also:** getCommentURL()

- getCommentURL

```java
public
String
getCommentURL()
```

Returns the comment URL describing the purpose of this cookie, or

null

if the cookie has no comment URL.

**Returns:** a

String

containing the comment URL, or

null

if none
**See Also:** setCommentURL(java.lang.String)

- setDiscard

```java
public void setDiscard​(boolean discard)
```

Specify whether user agent should discard the cookie unconditionally.
This is RFC 2965 only attribute.

**Parameters:** discard

-

true

indicates to discard cookie unconditionally
**See Also:** getDiscard()

- getDiscard

```java
public boolean getDiscard()
```

Returns the discard attribute of the cookie

**Returns:** a

boolean

to represent this cookie's discard attribute
**See Also:** setDiscard(boolean)

- setPortlist

```java
public void setPortlist​(
String
ports)
```

Specify the portlist of the cookie, which restricts the port(s)
to which a cookie may be sent back in a Cookie header.

**Parameters:** ports

- a

String

specify the port list, which is comma separated
series of digits
**See Also:** getPortlist()

- getPortlist

```java
public
String
getPortlist()
```

Returns the port list attribute of the cookie

**Returns:** a

String

contains the port list or

null

if none
**See Also:** setPortlist(java.lang.String)

- setDomain

```java
public void setDomain​(
String
pattern)
```

Specifies the domain within which this cookie should be presented.

The form of the domain name is specified by RFC 2965. A domain
name begins with a dot (

.foo.com

) and means that
the cookie is visible to servers in a specified Domain Name System
(DNS) zone (for example,

www.foo.com

, but not

a.b.foo.com

). By default, cookies are only returned
to the server that sent them.

**Parameters:** pattern

- a

String

containing the domain name within which this
cookie is visible; form is according to RFC 2965
**See Also:** getDomain()

- getDomain

```java
public
String
getDomain()
```

Returns the domain name set for this cookie. The form of the domain name
is set by RFC 2965.

**Returns:** a

String

containing the domain name
**See Also:** setDomain(java.lang.String)

- setMaxAge

```java
public void setMaxAge​(long expiry)
```

Sets the maximum age of the cookie in seconds.

A positive value indicates that the cookie will expire
after that many seconds have passed. Note that the value is
the

maximum

age when the cookie will expire, not the cookie's
current age.

A negative value means that the cookie is not stored persistently
and will be deleted when the Web browser exits. A zero value causes the
cookie to be deleted.

**Parameters:** expiry

- an integer specifying the maximum age of the cookie in seconds;
if zero, the cookie should be discarded immediately; otherwise,
the cookie's max age is unspecified.
**See Also:** getMaxAge()

- getMaxAge

```java
public long getMaxAge()
```

Returns the maximum age of the cookie, specified in seconds. By default,

-1

indicating the cookie will persist until browser shutdown.

**Returns:** an integer specifying the maximum age of the cookie in seconds
**See Also:** setMaxAge(long)

- setPath

```java
public void setPath​(
String
uri)
```

Specifies a path for the cookie to which the client should return
the cookie.

The cookie is visible to all the pages in the directory
you specify, and all the pages in that directory's subdirectories.
A cookie's path must include the servlet that set the cookie,
for example,

/catalog

, which makes the cookie
visible to all directories on the server under

/catalog

.

Consult RFC 2965 (available on the Internet) for more
information on setting path names for cookies.

**Parameters:** uri

- a

String

specifying a path
**See Also:** getPath()

- getPath

```java
public
String
getPath()
```

Returns the path on the server to which the browser returns this cookie.
The cookie is visible to all subpaths on the server.

**Returns:** a

String

specifying a path that contains a servlet name,
for example,

/catalog
**See Also:** setPath(java.lang.String)

- setSecure

```java
public void setSecure​(boolean flag)
```

Indicates whether the cookie should only be sent using a secure protocol,
such as HTTPS or SSL.

The default value is

false

.

**Parameters:** flag

- If

true

, the cookie can only be sent over a secure
protocol like HTTPS. If

false

, it can be sent over
any protocol.
**See Also:** getSecure()

- getSecure

```java
public boolean getSecure()
```

Returns

true

if sending this cookie should be restricted to a
secure protocol, or

false

if the it can be sent using any
protocol.

**Returns:** false

if the cookie can be sent over any standard
protocol; otherwise,

true
**See Also:** setSecure(boolean)

- getName

```java
public
String
getName()
```

Returns the name of the cookie. The name cannot be changed after
creation.

**Returns:** a

String

specifying the cookie's name

- setValue

```java
public void setValue​(
String
newValue)
```

Assigns a new value to a cookie after the cookie is created.
If you use a binary value, you may want to use BASE64 encoding.

With Version 0 cookies, values should not contain white space,
brackets, parentheses, equals signs, commas, double quotes, slashes,
question marks, at signs, colons, and semicolons. Empty values may not
behave the same way on all browsers.

**Parameters:** newValue

- a

String

specifying the new value
**See Also:** getValue()

- getValue

```java
public
String
getValue()
```

Returns the value of the cookie.

**Returns:** a

String

containing the cookie's present value
**See Also:** setValue(java.lang.String)

- getVersion

```java
public int getVersion()
```

Returns the version of the protocol this cookie complies with. Version 1
complies with RFC 2965/2109, and version 0 complies with the original
cookie specification drafted by Netscape. Cookies provided by a browser
use and identify the browser's cookie version.

**Returns:** 0 if the cookie complies with the original Netscape
specification; 1 if the cookie complies with RFC 2965/2109
**See Also:** setVersion(int)

- setVersion

```java
public void setVersion​(int v)
```

Sets the version of the cookie protocol this cookie complies
with. Version 0 complies with the original Netscape cookie
specification. Version 1 complies with RFC 2965/2109.

**Parameters:** v

- 0 if the cookie should comply with the original Netscape
specification; 1 if the cookie should comply with RFC 2965/2109
**Throws:** IllegalArgumentException

- if

v

is neither 0 nor 1
**See Also:** getVersion()

- isHttpOnly

```java
public boolean isHttpOnly()
```

Returns

true

if this cookie contains the

HttpOnly

attribute. This means that the cookie should not be accessible to
scripting engines, like javascript.

**Returns:** true

if this cookie should be considered HTTPOnly
**See Also:** setHttpOnly(boolean)

- setHttpOnly

```java
public void setHttpOnly​(boolean httpOnly)
```

Indicates whether the cookie should be considered HTTP Only. If set to

true

it means the cookie should not be accessible to scripting
engines like javascript.

**Parameters:** httpOnly

- if

true

make the cookie HTTP only, i.e. only visible as
part of an HTTP request.
**See Also:** isHttpOnly()

- domainMatches

```java
public static boolean domainMatches​(
String
domain,

String
host)
```

The utility method to check whether a host name is in a domain or not.

This concept is described in the cookie specification.
To understand the concept, some terminologies need to be defined first:

effective host name = hostname if host name contains dot

or = hostname.local if not

Host A's name domain-matches host B's if:

- their host name strings string-compare equal; or
- A is a HDN string and has the form NB, where N is a non-empty
name string, B has the form .B', and B' is a HDN string. (So,
x.y.com domain-matches .Y.com but not Y.com.)

A host isn't in a domain (RFC 2965 sec. 3.3.2) if:

- The value for the Domain attribute contains no embedded dots,
and the value is not .local.
- The effective host name that derives from the request-host does
not domain-match the Domain attribute.
- The request-host is a HDN (not IP address) and has the form HD,
where D is the value of the Domain attribute, and H is a string
that contains one or more dots.

Examples:

- A Set-Cookie2 from request-host y.x.foo.com for Domain=.foo.com
would be rejected, because H is y.x and contains a dot.
- A Set-Cookie2 from request-host x.foo.com for Domain=.foo.com
would be accepted.
- A Set-Cookie2 with Domain=.com or Domain=.com., will always be
rejected, because there is no embedded dot.
- A Set-Cookie2 from request-host example for Domain=.local will
be accepted, because the effective host name for the request-
host is example.local, and example.local domain-matches .local.

**Parameters:** domain

- the domain name to check host name with
**Parameters:** host

- the host name in question
**Returns:** true

if they domain-matches;

false

if not

- toString

```java
public
String
toString()
```

Constructs a cookie header string representation of this cookie,
which is in the format defined by corresponding cookie specification,
but without the leading "Cookie:" token.

**Overrides:** toString

in class

Object
**Returns:** a string form of the cookie. The string has the defined format

- equals

```java
public boolean equals​(
Object
obj)
```

Test the equality of two HTTP cookies.

The result is

true

only if two cookies come from same domain
(case-insensitive), have same name (case-insensitive), and have same path
(case-sensitive).

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if two HTTP cookies equal to each other;
otherwise,

false
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code of this HTTP cookie. The result is the sum of
hash code value of three significant components of this cookie: name,
domain, and path. That is, the hash code is the value of the expression:

getName().toLowerCase().hashCode()

+ getDomain().toLowerCase().hashCode()

+ getPath().hashCode()

**Overrides:** hashCode

in class

Object
**Returns:** this HTTP cookie's hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Create and return a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this HTTP cookie
**See Also:** Cloneable

---

#### Method Detail

parse

```java
public static
List
<
HttpCookie
> parse​(
String
header)
```

Constructs cookies from set-cookie or set-cookie2 header string.
RFC 2965 section 3.2.2 set-cookie2 syntax indicates that one header line
may contain more than one cookie definitions, so this is a static
utility method instead of another constructor.

**Parameters:** header

- a

String

specifying the set-cookie header. The header
should start with "set-cookie", or "set-cookie2" token; or it
should have no leading token at all.
**Returns:** a List of cookie parsed from header line string
**Throws:** IllegalArgumentException

- if header string violates the cookie specification's syntax or
the cookie name contains illegal characters.
**Throws:** NullPointerException

- if the header string is

null

---

#### parse

public static

List

<

HttpCookie

> parse​(

String

header)

Constructs cookies from set-cookie or set-cookie2 header string.
RFC 2965 section 3.2.2 set-cookie2 syntax indicates that one header line
may contain more than one cookie definitions, so this is a static
utility method instead of another constructor.

hasExpired

```java
public boolean hasExpired()
```

Reports whether this HTTP cookie has expired or not.

**Returns:** true

to indicate this HTTP cookie has expired;
otherwise,

false

---

#### hasExpired

public boolean hasExpired()

Reports whether this HTTP cookie has expired or not.

setComment

```java
public void setComment​(
String
purpose)
```

Specifies a comment that describes a cookie's purpose.
The comment is useful if the browser presents the cookie
to the user. Comments are not supported by Netscape Version 0 cookies.

**Parameters:** purpose

- a

String

specifying the comment to display to the user
**See Also:** getComment()

---

#### setComment

public void setComment​(

String

purpose)

Specifies a comment that describes a cookie's purpose.
The comment is useful if the browser presents the cookie
to the user. Comments are not supported by Netscape Version 0 cookies.

getComment

```java
public
String
getComment()
```

Returns the comment describing the purpose of this cookie, or

null

if the cookie has no comment.

**Returns:** a

String

containing the comment, or

null

if none
**See Also:** setComment(java.lang.String)

---

#### getComment

public

String

getComment()

Returns the comment describing the purpose of this cookie, or

null

if the cookie has no comment.

setCommentURL

```java
public void setCommentURL​(
String
purpose)
```

Specifies a comment URL that describes a cookie's purpose.
The comment URL is useful if the browser presents the cookie
to the user. Comment URL is RFC 2965 only.

**Parameters:** purpose

- a

String

specifying the comment URL to display to the user
**See Also:** getCommentURL()

---

#### setCommentURL

public void setCommentURL​(

String

purpose)

Specifies a comment URL that describes a cookie's purpose.
The comment URL is useful if the browser presents the cookie
to the user. Comment URL is RFC 2965 only.

getCommentURL

```java
public
String
getCommentURL()
```

Returns the comment URL describing the purpose of this cookie, or

null

if the cookie has no comment URL.

**Returns:** a

String

containing the comment URL, or

null

if none
**See Also:** setCommentURL(java.lang.String)

---

#### getCommentURL

public

String

getCommentURL()

Returns the comment URL describing the purpose of this cookie, or

null

if the cookie has no comment URL.

setDiscard

```java
public void setDiscard​(boolean discard)
```

Specify whether user agent should discard the cookie unconditionally.
This is RFC 2965 only attribute.

**Parameters:** discard

-

true

indicates to discard cookie unconditionally
**See Also:** getDiscard()

---

#### setDiscard

public void setDiscard​(boolean discard)

Specify whether user agent should discard the cookie unconditionally.
This is RFC 2965 only attribute.

getDiscard

```java
public boolean getDiscard()
```

Returns the discard attribute of the cookie

**Returns:** a

boolean

to represent this cookie's discard attribute
**See Also:** setDiscard(boolean)

---

#### getDiscard

public boolean getDiscard()

Returns the discard attribute of the cookie

setPortlist

```java
public void setPortlist​(
String
ports)
```

Specify the portlist of the cookie, which restricts the port(s)
to which a cookie may be sent back in a Cookie header.

**Parameters:** ports

- a

String

specify the port list, which is comma separated
series of digits
**See Also:** getPortlist()

---

#### setPortlist

public void setPortlist​(

String

ports)

Specify the portlist of the cookie, which restricts the port(s)
to which a cookie may be sent back in a Cookie header.

getPortlist

```java
public
String
getPortlist()
```

Returns the port list attribute of the cookie

**Returns:** a

String

contains the port list or

null

if none
**See Also:** setPortlist(java.lang.String)

---

#### getPortlist

public

String

getPortlist()

Returns the port list attribute of the cookie

setDomain

```java
public void setDomain​(
String
pattern)
```

Specifies the domain within which this cookie should be presented.

The form of the domain name is specified by RFC 2965. A domain
name begins with a dot (

.foo.com

) and means that
the cookie is visible to servers in a specified Domain Name System
(DNS) zone (for example,

www.foo.com

, but not

a.b.foo.com

). By default, cookies are only returned
to the server that sent them.

**Parameters:** pattern

- a

String

containing the domain name within which this
cookie is visible; form is according to RFC 2965
**See Also:** getDomain()

---

#### setDomain

public void setDomain​(

String

pattern)

Specifies the domain within which this cookie should be presented.

The form of the domain name is specified by RFC 2965. A domain
name begins with a dot (

.foo.com

) and means that
the cookie is visible to servers in a specified Domain Name System
(DNS) zone (for example,

www.foo.com

, but not

a.b.foo.com

). By default, cookies are only returned
to the server that sent them.

The form of the domain name is specified by RFC 2965. A domain
name begins with a dot (

.foo.com

) and means that
the cookie is visible to servers in a specified Domain Name System
(DNS) zone (for example,

www.foo.com

, but not

a.b.foo.com

). By default, cookies are only returned
to the server that sent them.

getDomain

```java
public
String
getDomain()
```

Returns the domain name set for this cookie. The form of the domain name
is set by RFC 2965.

**Returns:** a

String

containing the domain name
**See Also:** setDomain(java.lang.String)

---

#### getDomain

public

String

getDomain()

Returns the domain name set for this cookie. The form of the domain name
is set by RFC 2965.

setMaxAge

```java
public void setMaxAge​(long expiry)
```

Sets the maximum age of the cookie in seconds.

A positive value indicates that the cookie will expire
after that many seconds have passed. Note that the value is
the

maximum

age when the cookie will expire, not the cookie's
current age.

A negative value means that the cookie is not stored persistently
and will be deleted when the Web browser exits. A zero value causes the
cookie to be deleted.

**Parameters:** expiry

- an integer specifying the maximum age of the cookie in seconds;
if zero, the cookie should be discarded immediately; otherwise,
the cookie's max age is unspecified.
**See Also:** getMaxAge()

---

#### setMaxAge

public void setMaxAge​(long expiry)

Sets the maximum age of the cookie in seconds.

A positive value indicates that the cookie will expire
after that many seconds have passed. Note that the value is
the

maximum

age when the cookie will expire, not the cookie's
current age.

A negative value means that the cookie is not stored persistently
and will be deleted when the Web browser exits. A zero value causes the
cookie to be deleted.

A positive value indicates that the cookie will expire
after that many seconds have passed. Note that the value is
the

maximum

age when the cookie will expire, not the cookie's
current age.

A negative value means that the cookie is not stored persistently
and will be deleted when the Web browser exits. A zero value causes the
cookie to be deleted.

A negative value means that the cookie is not stored persistently
and will be deleted when the Web browser exits. A zero value causes the
cookie to be deleted.

getMaxAge

```java
public long getMaxAge()
```

Returns the maximum age of the cookie, specified in seconds. By default,

-1

indicating the cookie will persist until browser shutdown.

**Returns:** an integer specifying the maximum age of the cookie in seconds
**See Also:** setMaxAge(long)

---

#### getMaxAge

public long getMaxAge()

Returns the maximum age of the cookie, specified in seconds. By default,

-1

indicating the cookie will persist until browser shutdown.

setPath

```java
public void setPath​(
String
uri)
```

Specifies a path for the cookie to which the client should return
the cookie.

The cookie is visible to all the pages in the directory
you specify, and all the pages in that directory's subdirectories.
A cookie's path must include the servlet that set the cookie,
for example,

/catalog

, which makes the cookie
visible to all directories on the server under

/catalog

.

Consult RFC 2965 (available on the Internet) for more
information on setting path names for cookies.

**Parameters:** uri

- a

String

specifying a path
**See Also:** getPath()

---

#### setPath

public void setPath​(

String

uri)

Specifies a path for the cookie to which the client should return
the cookie.

The cookie is visible to all the pages in the directory
you specify, and all the pages in that directory's subdirectories.
A cookie's path must include the servlet that set the cookie,
for example,

/catalog

, which makes the cookie
visible to all directories on the server under

/catalog

.

Consult RFC 2965 (available on the Internet) for more
information on setting path names for cookies.

The cookie is visible to all the pages in the directory
you specify, and all the pages in that directory's subdirectories.
A cookie's path must include the servlet that set the cookie,
for example,

/catalog

, which makes the cookie
visible to all directories on the server under

/catalog

.

Consult RFC 2965 (available on the Internet) for more
information on setting path names for cookies.

Consult RFC 2965 (available on the Internet) for more
information on setting path names for cookies.

getPath

```java
public
String
getPath()
```

Returns the path on the server to which the browser returns this cookie.
The cookie is visible to all subpaths on the server.

**Returns:** a

String

specifying a path that contains a servlet name,
for example,

/catalog
**See Also:** setPath(java.lang.String)

---

#### getPath

public

String

getPath()

Returns the path on the server to which the browser returns this cookie.
The cookie is visible to all subpaths on the server.

setSecure

```java
public void setSecure​(boolean flag)
```

Indicates whether the cookie should only be sent using a secure protocol,
such as HTTPS or SSL.

The default value is

false

.

**Parameters:** flag

- If

true

, the cookie can only be sent over a secure
protocol like HTTPS. If

false

, it can be sent over
any protocol.
**See Also:** getSecure()

---

#### setSecure

public void setSecure​(boolean flag)

Indicates whether the cookie should only be sent using a secure protocol,
such as HTTPS or SSL.

The default value is

false

.

The default value is

false

.

getSecure

```java
public boolean getSecure()
```

Returns

true

if sending this cookie should be restricted to a
secure protocol, or

false

if the it can be sent using any
protocol.

**Returns:** false

if the cookie can be sent over any standard
protocol; otherwise,

true
**See Also:** setSecure(boolean)

---

#### getSecure

public boolean getSecure()

Returns

true

if sending this cookie should be restricted to a
secure protocol, or

false

if the it can be sent using any
protocol.

getName

```java
public
String
getName()
```

Returns the name of the cookie. The name cannot be changed after
creation.

**Returns:** a

String

specifying the cookie's name

---

#### getName

public

String

getName()

Returns the name of the cookie. The name cannot be changed after
creation.

setValue

```java
public void setValue​(
String
newValue)
```

Assigns a new value to a cookie after the cookie is created.
If you use a binary value, you may want to use BASE64 encoding.

With Version 0 cookies, values should not contain white space,
brackets, parentheses, equals signs, commas, double quotes, slashes,
question marks, at signs, colons, and semicolons. Empty values may not
behave the same way on all browsers.

**Parameters:** newValue

- a

String

specifying the new value
**See Also:** getValue()

---

#### setValue

public void setValue​(

String

newValue)

Assigns a new value to a cookie after the cookie is created.
If you use a binary value, you may want to use BASE64 encoding.

With Version 0 cookies, values should not contain white space,
brackets, parentheses, equals signs, commas, double quotes, slashes,
question marks, at signs, colons, and semicolons. Empty values may not
behave the same way on all browsers.

With Version 0 cookies, values should not contain white space,
brackets, parentheses, equals signs, commas, double quotes, slashes,
question marks, at signs, colons, and semicolons. Empty values may not
behave the same way on all browsers.

getValue

```java
public
String
getValue()
```

Returns the value of the cookie.

**Returns:** a

String

containing the cookie's present value
**See Also:** setValue(java.lang.String)

---

#### getValue

public

String

getValue()

Returns the value of the cookie.

getVersion

```java
public int getVersion()
```

Returns the version of the protocol this cookie complies with. Version 1
complies with RFC 2965/2109, and version 0 complies with the original
cookie specification drafted by Netscape. Cookies provided by a browser
use and identify the browser's cookie version.

**Returns:** 0 if the cookie complies with the original Netscape
specification; 1 if the cookie complies with RFC 2965/2109
**See Also:** setVersion(int)

---

#### getVersion

public int getVersion()

Returns the version of the protocol this cookie complies with. Version 1
complies with RFC 2965/2109, and version 0 complies with the original
cookie specification drafted by Netscape. Cookies provided by a browser
use and identify the browser's cookie version.

setVersion

```java
public void setVersion​(int v)
```

Sets the version of the cookie protocol this cookie complies
with. Version 0 complies with the original Netscape cookie
specification. Version 1 complies with RFC 2965/2109.

**Parameters:** v

- 0 if the cookie should comply with the original Netscape
specification; 1 if the cookie should comply with RFC 2965/2109
**Throws:** IllegalArgumentException

- if

v

is neither 0 nor 1
**See Also:** getVersion()

---

#### setVersion

public void setVersion​(int v)

Sets the version of the cookie protocol this cookie complies
with. Version 0 complies with the original Netscape cookie
specification. Version 1 complies with RFC 2965/2109.

isHttpOnly

```java
public boolean isHttpOnly()
```

Returns

true

if this cookie contains the

HttpOnly

attribute. This means that the cookie should not be accessible to
scripting engines, like javascript.

**Returns:** true

if this cookie should be considered HTTPOnly
**See Also:** setHttpOnly(boolean)

---

#### isHttpOnly

public boolean isHttpOnly()

Returns

true

if this cookie contains the

HttpOnly

attribute. This means that the cookie should not be accessible to
scripting engines, like javascript.

setHttpOnly

```java
public void setHttpOnly​(boolean httpOnly)
```

Indicates whether the cookie should be considered HTTP Only. If set to

true

it means the cookie should not be accessible to scripting
engines like javascript.

**Parameters:** httpOnly

- if

true

make the cookie HTTP only, i.e. only visible as
part of an HTTP request.
**See Also:** isHttpOnly()

---

#### setHttpOnly

public void setHttpOnly​(boolean httpOnly)

Indicates whether the cookie should be considered HTTP Only. If set to

true

it means the cookie should not be accessible to scripting
engines like javascript.

domainMatches

```java
public static boolean domainMatches​(
String
domain,

String
host)
```

The utility method to check whether a host name is in a domain or not.

This concept is described in the cookie specification.
To understand the concept, some terminologies need to be defined first:

effective host name = hostname if host name contains dot

or = hostname.local if not

Host A's name domain-matches host B's if:

- their host name strings string-compare equal; or
- A is a HDN string and has the form NB, where N is a non-empty
name string, B has the form .B', and B' is a HDN string. (So,
x.y.com domain-matches .Y.com but not Y.com.)

A host isn't in a domain (RFC 2965 sec. 3.3.2) if:

- The value for the Domain attribute contains no embedded dots,
and the value is not .local.
- The effective host name that derives from the request-host does
not domain-match the Domain attribute.
- The request-host is a HDN (not IP address) and has the form HD,
where D is the value of the Domain attribute, and H is a string
that contains one or more dots.

Examples:

- A Set-Cookie2 from request-host y.x.foo.com for Domain=.foo.com
would be rejected, because H is y.x and contains a dot.
- A Set-Cookie2 from request-host x.foo.com for Domain=.foo.com
would be accepted.
- A Set-Cookie2 with Domain=.com or Domain=.com., will always be
rejected, because there is no embedded dot.
- A Set-Cookie2 from request-host example for Domain=.local will
be accepted, because the effective host name for the request-
host is example.local, and example.local domain-matches .local.

**Parameters:** domain

- the domain name to check host name with
**Parameters:** host

- the host name in question
**Returns:** true

if they domain-matches;

false

if not

---

#### domainMatches

public static boolean domainMatches​(

String

domain,

String

host)

The utility method to check whether a host name is in a domain or not.

This concept is described in the cookie specification.
To understand the concept, some terminologies need to be defined first:

effective host name = hostname if host name contains dot

or = hostname.local if not

Host A's name domain-matches host B's if:

- their host name strings string-compare equal; or
- A is a HDN string and has the form NB, where N is a non-empty
name string, B has the form .B', and B' is a HDN string. (So,
x.y.com domain-matches .Y.com but not Y.com.)

A host isn't in a domain (RFC 2965 sec. 3.3.2) if:

- The value for the Domain attribute contains no embedded dots,
and the value is not .local.
- The effective host name that derives from the request-host does
not domain-match the Domain attribute.
- The request-host is a HDN (not IP address) and has the form HD,
where D is the value of the Domain attribute, and H is a string
that contains one or more dots.

Examples:

- A Set-Cookie2 from request-host y.x.foo.com for Domain=.foo.com
would be rejected, because H is y.x and contains a dot.
- A Set-Cookie2 from request-host x.foo.com for Domain=.foo.com
would be accepted.
- A Set-Cookie2 with Domain=.com or Domain=.com., will always be
rejected, because there is no embedded dot.
- A Set-Cookie2 from request-host example for Domain=.local will
be accepted, because the effective host name for the request-
host is example.local, and example.local domain-matches .local.

This concept is described in the cookie specification.
To understand the concept, some terminologies need to be defined first:

effective host name = hostname if host name contains dot

or = hostname.local if not

Host A's name domain-matches host B's if:

- their host name strings string-compare equal; or
- A is a HDN string and has the form NB, where N is a non-empty
name string, B has the form .B', and B' is a HDN string. (So,
x.y.com domain-matches .Y.com but not Y.com.)

A host isn't in a domain (RFC 2965 sec. 3.3.2) if:

- The value for the Domain attribute contains no embedded dots,
and the value is not .local.
- The effective host name that derives from the request-host does
not domain-match the Domain attribute.
- The request-host is a HDN (not IP address) and has the form HD,
where D is the value of the Domain attribute, and H is a string
that contains one or more dots.

Examples:

- A Set-Cookie2 from request-host y.x.foo.com for Domain=.foo.com
would be rejected, because H is y.x and contains a dot.
- A Set-Cookie2 from request-host x.foo.com for Domain=.foo.com
would be accepted.
- A Set-Cookie2 with Domain=.com or Domain=.com., will always be
rejected, because there is no embedded dot.
- A Set-Cookie2 from request-host example for Domain=.local will
be accepted, because the effective host name for the request-
host is example.local, and example.local domain-matches .local.

Host A's name domain-matches host B's if:

- their host name strings string-compare equal; or
- A is a HDN string and has the form NB, where N is a non-empty
name string, B has the form .B', and B' is a HDN string. (So,
x.y.com domain-matches .Y.com but not Y.com.)

A host isn't in a domain (RFC 2965 sec. 3.3.2) if:

- The value for the Domain attribute contains no embedded dots,
and the value is not .local.
- The effective host name that derives from the request-host does
not domain-match the Domain attribute.
- The request-host is a HDN (not IP address) and has the form HD,
where D is the value of the Domain attribute, and H is a string
that contains one or more dots.

Examples:

- A Set-Cookie2 from request-host y.x.foo.com for Domain=.foo.com
would be rejected, because H is y.x and contains a dot.
- A Set-Cookie2 from request-host x.foo.com for Domain=.foo.com
would be accepted.
- A Set-Cookie2 with Domain=.com or Domain=.com., will always be
rejected, because there is no embedded dot.
- A Set-Cookie2 from request-host example for Domain=.local will
be accepted, because the effective host name for the request-
host is example.local, and example.local domain-matches .local.

their host name strings string-compare equal; or

A is a HDN string and has the form NB, where N is a non-empty
name string, B has the form .B', and B' is a HDN string. (So,
x.y.com domain-matches .Y.com but not Y.com.)

A host isn't in a domain (RFC 2965 sec. 3.3.2) if:

- The value for the Domain attribute contains no embedded dots,
and the value is not .local.
- The effective host name that derives from the request-host does
not domain-match the Domain attribute.
- The request-host is a HDN (not IP address) and has the form HD,
where D is the value of the Domain attribute, and H is a string
that contains one or more dots.

Examples:

- A Set-Cookie2 from request-host y.x.foo.com for Domain=.foo.com
would be rejected, because H is y.x and contains a dot.
- A Set-Cookie2 from request-host x.foo.com for Domain=.foo.com
would be accepted.
- A Set-Cookie2 with Domain=.com or Domain=.com., will always be
rejected, because there is no embedded dot.
- A Set-Cookie2 from request-host example for Domain=.local will
be accepted, because the effective host name for the request-
host is example.local, and example.local domain-matches .local.

The value for the Domain attribute contains no embedded dots,
and the value is not .local.

The effective host name that derives from the request-host does
not domain-match the Domain attribute.

The request-host is a HDN (not IP address) and has the form HD,
where D is the value of the Domain attribute, and H is a string
that contains one or more dots.

Examples:

- A Set-Cookie2 from request-host y.x.foo.com for Domain=.foo.com
would be rejected, because H is y.x and contains a dot.
- A Set-Cookie2 from request-host x.foo.com for Domain=.foo.com
would be accepted.
- A Set-Cookie2 with Domain=.com or Domain=.com., will always be
rejected, because there is no embedded dot.
- A Set-Cookie2 from request-host example for Domain=.local will
be accepted, because the effective host name for the request-
host is example.local, and example.local domain-matches .local.

A Set-Cookie2 from request-host y.x.foo.com for Domain=.foo.com
would be rejected, because H is y.x and contains a dot.

A Set-Cookie2 from request-host x.foo.com for Domain=.foo.com
would be accepted.

A Set-Cookie2 with Domain=.com or Domain=.com., will always be
rejected, because there is no embedded dot.

A Set-Cookie2 from request-host example for Domain=.local will
be accepted, because the effective host name for the request-
host is example.local, and example.local domain-matches .local.

toString

```java
public
String
toString()
```

Constructs a cookie header string representation of this cookie,
which is in the format defined by corresponding cookie specification,
but without the leading "Cookie:" token.

**Overrides:** toString

in class

Object
**Returns:** a string form of the cookie. The string has the defined format

---

#### toString

public

String

toString()

Constructs a cookie header string representation of this cookie,
which is in the format defined by corresponding cookie specification,
but without the leading "Cookie:" token.

equals

```java
public boolean equals​(
Object
obj)
```

Test the equality of two HTTP cookies.

The result is

true

only if two cookies come from same domain
(case-insensitive), have same name (case-insensitive), and have same path
(case-sensitive).

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if two HTTP cookies equal to each other;
otherwise,

false
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Test the equality of two HTTP cookies.

The result is

true

only if two cookies come from same domain
(case-insensitive), have same name (case-insensitive), and have same path
(case-sensitive).

The result is

true

only if two cookies come from same domain
(case-insensitive), have same name (case-insensitive), and have same path
(case-sensitive).

hashCode

```java
public int hashCode()
```

Returns the hash code of this HTTP cookie. The result is the sum of
hash code value of three significant components of this cookie: name,
domain, and path. That is, the hash code is the value of the expression:

getName().toLowerCase().hashCode()

+ getDomain().toLowerCase().hashCode()

+ getPath().hashCode()

**Overrides:** hashCode

in class

Object
**Returns:** this HTTP cookie's hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code of this HTTP cookie. The result is the sum of
hash code value of three significant components of this cookie: name,
domain, and path. That is, the hash code is the value of the expression:

getName().toLowerCase().hashCode()

+ getDomain().toLowerCase().hashCode()

+ getPath().hashCode()

clone

```java
public
Object
clone()
```

Create and return a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this HTTP cookie
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Create and return a copy of this object.

---

