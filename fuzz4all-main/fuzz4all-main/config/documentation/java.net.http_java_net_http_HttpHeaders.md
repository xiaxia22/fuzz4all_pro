# Class HttpHeaders

**Source:** `java.net.http\java\net\http\HttpHeaders.html`

### Class Description

```java
public final class
HttpHeaders

extends
Object
```

A read-only view of a set of HTTP headers.

An

HttpHeaders

is not typically created directly, but rather
returned from an

HttpRequest

or an

HttpResponse

. Specific HTTP headers can be
set for a

request

through one of the request
builder's

headers

methods.

The methods of this class ( that accept a String header name ), and the

Map

returned by the

map

method, operate without regard
to case when retrieving the header value(s).

An HTTP header name may appear more than once in the HTTP protocol. As
such, headers are represented as a name and a list of values. Each occurrence
of a header value is added verbatim, to the appropriate header name list,
without interpreting its value. In particular,

HttpHeaders

does not
perform any splitting or joining of comma separated header value strings. The
order of elements in a header value list is preserved when

building

a request. For
responses, the order of elements in a header value list is the order in which
they were received. The

Map

returned by the

map

method,
however, does not provide any guarantee with regard to the ordering of its
entries.

HttpHeaders

instances are immutable.

**Since:** 11

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
Optional
<
String
> firstValue​(
String
name)

Returns an

Optional

containing the first header string value of
the given named (and possibly multi-valued) header. If the header is not
present, then the returned

Optional

is empty.

**Parameters:**
- name

- the header name

**Returns:**
- an

Optional<String>

containing the first named header
string value, if present

---

#### public
OptionalLong
firstValueAsLong​(
String
name)

Returns an

OptionalLong

containing the first header string value
of the named header field. If the header is not present, then the
Optional is empty. If the header is present but contains a value that
does not parse as a

Long

value, then an exception is thrown.

**Parameters:**
- name

- the header name

**Returns:**
- an

OptionalLong

**Throws:**
- NumberFormatException

- if a value is found, but does not parse as
a Long

---

#### public
List
<
String
> allValues​(
String
name)

Returns an unmodifiable List of all of the header string values of the
given named header. Always returns a List, which may be empty if the
header is not present.

**Parameters:**
- name

- the header name

**Returns:**
- a List of headers string values

---

#### public
Map
<
String
,​
List
<
String
>> map()

Returns an unmodifiable multi Map view of this HttpHeaders.

**Returns:**
- the Map

---

#### public final boolean equals​(
Object
obj)

Tests this HTTP headers instance for equality with the given object.

If the given object is not an

HttpHeaders

then this
method returns

false

. Two HTTP headers are equal if each
of their corresponding

maps

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to which this object is to be compared

**Returns:**
- true

if, and only if, the given object is an

HttpHeaders

that is equal to this HTTP headers

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Computes a hash code for this HTTP headers instance.

The hash code is based upon the components of the HTTP headers

map

, and satisfies the general contract of the

Object.hashCode

method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash-code value for this HTTP headers

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns this HTTP headers as a string.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string describing the HTTP headers

---

#### public static
HttpHeaders
of​(
Map
<
String
,​
List
<
String
>> headerMap,

BiPredicate
<
String
,​
String
> filter)

Returns an HTTP headers from the given map. The given map's key
represents the header name, and its value the list of string header
values for that header name.

An HTTP header name may appear more than once in the HTTP protocol.
Such,

multi-valued

, headers must be represented by a single entry
in the given map, whose entry value is a list that represents the
multiple header string values. Leading and trailing whitespaces are
removed from all string values retrieved from the given map and its lists
before processing. Only headers that, after filtering, contain at least
one, possibly empty string, value will be added to the HTTP headers.

**Parameters:**
- headerMap

- the map containing the header names and values
- filter

- a filter that can be used to inspect each
header-name-and-value pair in the given map to determine if
it should, or should not, be added to the to the HTTP
headers

**Returns:**
- an HTTP headers instance containing the given headers

**Throws:**
- NullPointerException

- if any of:

headerMap

, a key or value
in the given map, or an entry in the map's value list, or

filter

, is

null
- IllegalArgumentException

- if the given

headerMap

contains
any two keys that are equal ( without regard to case ); or if the
given map contains any key whose length, after trimming
whitespaces, is

0

**API Note:**
- The primary purpose of this method is for testing frameworks.
Per-request headers can be set through one of the

HttpRequest

headers

methods.

---

### Additional Sections

#### Class HttpHeaders

java.lang.Object

- java.net.http.HttpHeaders

java.net.http.HttpHeaders

```java
public final class
HttpHeaders

extends
Object
```

A read-only view of a set of HTTP headers.

An

HttpHeaders

is not typically created directly, but rather
returned from an

HttpRequest

or an

HttpResponse

. Specific HTTP headers can be
set for a

request

through one of the request
builder's

headers

methods.

The methods of this class ( that accept a String header name ), and the

Map

returned by the

map

method, operate without regard
to case when retrieving the header value(s).

An HTTP header name may appear more than once in the HTTP protocol. As
such, headers are represented as a name and a list of values. Each occurrence
of a header value is added verbatim, to the appropriate header name list,
without interpreting its value. In particular,

HttpHeaders

does not
perform any splitting or joining of comma separated header value strings. The
order of elements in a header value list is preserved when

building

a request. For
responses, the order of elements in a header value list is the order in which
they were received. The

Map

returned by the

map

method,
however, does not provide any guarantee with regard to the ordering of its
entries.

HttpHeaders

instances are immutable.

**Since:** 11

public final class

HttpHeaders

extends

Object

A read-only view of a set of HTTP headers.

An

HttpHeaders

is not typically created directly, but rather
returned from an

HttpRequest

or an

HttpResponse

. Specific HTTP headers can be
set for a

request

through one of the request
builder's

headers

methods.

The methods of this class ( that accept a String header name ), and the

Map

returned by the

map

method, operate without regard
to case when retrieving the header value(s).

An HTTP header name may appear more than once in the HTTP protocol. As
such, headers are represented as a name and a list of values. Each occurrence
of a header value is added verbatim, to the appropriate header name list,
without interpreting its value. In particular,

HttpHeaders

does not
perform any splitting or joining of comma separated header value strings. The
order of elements in a header value list is preserved when

building

a request. For
responses, the order of elements in a header value list is the order in which
they were received. The

Map

returned by the

map

method,
however, does not provide any guarantee with regard to the ordering of its
entries.

HttpHeaders

instances are immutable.

An

HttpHeaders

is not typically created directly, but rather
returned from an

HttpRequest

or an

HttpResponse

. Specific HTTP headers can be
set for a

request

through one of the request
builder's

headers

methods.

The methods of this class ( that accept a String header name ), and the

Map

returned by the

map

method, operate without regard
to case when retrieving the header value(s).

An HTTP header name may appear more than once in the HTTP protocol. As
such, headers are represented as a name and a list of values. Each occurrence
of a header value is added verbatim, to the appropriate header name list,
without interpreting its value. In particular,

HttpHeaders

does not
perform any splitting or joining of comma separated header value strings. The
order of elements in a header value list is preserved when

building

a request. For
responses, the order of elements in a header value list is the order in which
they were received. The

Map

returned by the

map

method,
however, does not provide any guarantee with regard to the ordering of its
entries.

HttpHeaders

instances are immutable.

The methods of this class ( that accept a String header name ), and the

Map

returned by the

map

method, operate without regard
to case when retrieving the header value(s).

An HTTP header name may appear more than once in the HTTP protocol. As
such, headers are represented as a name and a list of values. Each occurrence
of a header value is added verbatim, to the appropriate header name list,
without interpreting its value. In particular,

HttpHeaders

does not
perform any splitting or joining of comma separated header value strings. The
order of elements in a header value list is preserved when

building

a request. For
responses, the order of elements in a header value list is the order in which
they were received. The

Map

returned by the

map

method,
however, does not provide any guarantee with regard to the ordering of its
entries.

HttpHeaders

instances are immutable.

An HTTP header name may appear more than once in the HTTP protocol. As
such, headers are represented as a name and a list of values. Each occurrence
of a header value is added verbatim, to the appropriate header name list,
without interpreting its value. In particular,

HttpHeaders

does not
perform any splitting or joining of comma separated header value strings. The
order of elements in a header value list is preserved when

building

a request. For
responses, the order of elements in a header value list is the order in which
they were received. The

Map

returned by the

map

method,
however, does not provide any guarantee with regard to the ordering of its
entries.

HttpHeaders

instances are immutable.

HttpHeaders

instances are immutable.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

String

>

allValues

​(

String

name)

Returns an unmodifiable List of all of the header string values of the
given named header.

boolean

equals

​(

Object

obj)

Tests this HTTP headers instance for equality with the given object.

Optional

<

String

>

firstValue

​(

String

name)

Returns an

Optional

containing the first header string value of
the given named (and possibly multi-valued) header.

OptionalLong

firstValueAsLong

​(

String

name)

Returns an

OptionalLong

containing the first header string value
of the named header field.

int

hashCode

()

Computes a hash code for this HTTP headers instance.

Map

<

String

,​

List

<

String

>>

map

()

Returns an unmodifiable multi Map view of this HttpHeaders.

static

HttpHeaders

of

​(

Map

<

String

,​

List

<

String

>> headerMap,

BiPredicate

<

String

,​

String

> filter)

Returns an HTTP headers from the given map.

String

toString

()

Returns this HTTP headers as a string.

- Methods declared in class java.lang.

Object

clone

,

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

String

>

allValues

​(

String

name)

Returns an unmodifiable List of all of the header string values of the
given named header.

boolean

equals

​(

Object

obj)

Tests this HTTP headers instance for equality with the given object.

Optional

<

String

>

firstValue

​(

String

name)

Returns an

Optional

containing the first header string value of
the given named (and possibly multi-valued) header.

OptionalLong

firstValueAsLong

​(

String

name)

Returns an

OptionalLong

containing the first header string value
of the named header field.

int

hashCode

()

Computes a hash code for this HTTP headers instance.

Map

<

String

,​

List

<

String

>>

map

()

Returns an unmodifiable multi Map view of this HttpHeaders.

static

HttpHeaders

of

​(

Map

<

String

,​

List

<

String

>> headerMap,

BiPredicate

<

String

,​

String

> filter)

Returns an HTTP headers from the given map.

String

toString

()

Returns this HTTP headers as a string.

- Methods declared in class java.lang.

Object

clone

,

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

Returns an unmodifiable List of all of the header string values of the
given named header.

Tests this HTTP headers instance for equality with the given object.

Returns an

Optional

containing the first header string value of
the given named (and possibly multi-valued) header.

Returns an

OptionalLong

containing the first header string value
of the named header field.

Computes a hash code for this HTTP headers instance.

Returns an unmodifiable multi Map view of this HttpHeaders.

Returns an HTTP headers from the given map.

Returns this HTTP headers as a string.

Methods declared in class java.lang.

Object

clone

,

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

============ METHOD DETAIL ==========

- Method Detail

- firstValue

```java
public
Optional
<
String
> firstValue​(
String
name)
```

Returns an

Optional

containing the first header string value of
the given named (and possibly multi-valued) header. If the header is not
present, then the returned

Optional

is empty.

**Parameters:** name

- the header name
**Returns:** an

Optional<String>

containing the first named header
string value, if present

- firstValueAsLong

```java
public
OptionalLong
firstValueAsLong​(
String
name)
```

Returns an

OptionalLong

containing the first header string value
of the named header field. If the header is not present, then the
Optional is empty. If the header is present but contains a value that
does not parse as a

Long

value, then an exception is thrown.

**Parameters:** name

- the header name
**Returns:** an

OptionalLong
**Throws:** NumberFormatException

- if a value is found, but does not parse as
a Long

- allValues

```java
public
List
<
String
> allValues​(
String
name)
```

Returns an unmodifiable List of all of the header string values of the
given named header. Always returns a List, which may be empty if the
header is not present.

**Parameters:** name

- the header name
**Returns:** a List of headers string values

- map

```java
public
Map
<
String
,​
List
<
String
>> map()
```

Returns an unmodifiable multi Map view of this HttpHeaders.

**Returns:** the Map

- equals

```java
public final boolean equals​(
Object
obj)
```

Tests this HTTP headers instance for equality with the given object.

If the given object is not an

HttpHeaders

then this
method returns

false

. Two HTTP headers are equal if each
of their corresponding

maps

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is an

HttpHeaders

that is equal to this HTTP headers
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Computes a hash code for this HTTP headers instance.

The hash code is based upon the components of the HTTP headers

map

, and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** the hash-code value for this HTTP headers
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns this HTTP headers as a string.

**Overrides:** toString

in class

Object
**Returns:** a string describing the HTTP headers

- of

```java
public static
HttpHeaders
of​(
Map
<
String
,​
List
<
String
>> headerMap,

BiPredicate
<
String
,​
String
> filter)
```

Returns an HTTP headers from the given map. The given map's key
represents the header name, and its value the list of string header
values for that header name.

An HTTP header name may appear more than once in the HTTP protocol.
Such,

multi-valued

, headers must be represented by a single entry
in the given map, whose entry value is a list that represents the
multiple header string values. Leading and trailing whitespaces are
removed from all string values retrieved from the given map and its lists
before processing. Only headers that, after filtering, contain at least
one, possibly empty string, value will be added to the HTTP headers.

**API Note:** The primary purpose of this method is for testing frameworks.
Per-request headers can be set through one of the

HttpRequest

headers

methods.
**Parameters:** headerMap

- the map containing the header names and values
**Parameters:** filter

- a filter that can be used to inspect each
header-name-and-value pair in the given map to determine if
it should, or should not, be added to the to the HTTP
headers
**Returns:** an HTTP headers instance containing the given headers
**Throws:** NullPointerException

- if any of:

headerMap

, a key or value
in the given map, or an entry in the map's value list, or

filter

, is

null
**Throws:** IllegalArgumentException

- if the given

headerMap

contains
any two keys that are equal ( without regard to case ); or if the
given map contains any key whose length, after trimming
whitespaces, is

0

Method Detail

- firstValue

```java
public
Optional
<
String
> firstValue​(
String
name)
```

Returns an

Optional

containing the first header string value of
the given named (and possibly multi-valued) header. If the header is not
present, then the returned

Optional

is empty.

**Parameters:** name

- the header name
**Returns:** an

Optional<String>

containing the first named header
string value, if present

- firstValueAsLong

```java
public
OptionalLong
firstValueAsLong​(
String
name)
```

Returns an

OptionalLong

containing the first header string value
of the named header field. If the header is not present, then the
Optional is empty. If the header is present but contains a value that
does not parse as a

Long

value, then an exception is thrown.

**Parameters:** name

- the header name
**Returns:** an

OptionalLong
**Throws:** NumberFormatException

- if a value is found, but does not parse as
a Long

- allValues

```java
public
List
<
String
> allValues​(
String
name)
```

Returns an unmodifiable List of all of the header string values of the
given named header. Always returns a List, which may be empty if the
header is not present.

**Parameters:** name

- the header name
**Returns:** a List of headers string values

- map

```java
public
Map
<
String
,​
List
<
String
>> map()
```

Returns an unmodifiable multi Map view of this HttpHeaders.

**Returns:** the Map

- equals

```java
public final boolean equals​(
Object
obj)
```

Tests this HTTP headers instance for equality with the given object.

If the given object is not an

HttpHeaders

then this
method returns

false

. Two HTTP headers are equal if each
of their corresponding

maps

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is an

HttpHeaders

that is equal to this HTTP headers
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Computes a hash code for this HTTP headers instance.

The hash code is based upon the components of the HTTP headers

map

, and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** the hash-code value for this HTTP headers
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns this HTTP headers as a string.

**Overrides:** toString

in class

Object
**Returns:** a string describing the HTTP headers

- of

```java
public static
HttpHeaders
of​(
Map
<
String
,​
List
<
String
>> headerMap,

BiPredicate
<
String
,​
String
> filter)
```

Returns an HTTP headers from the given map. The given map's key
represents the header name, and its value the list of string header
values for that header name.

An HTTP header name may appear more than once in the HTTP protocol.
Such,

multi-valued

, headers must be represented by a single entry
in the given map, whose entry value is a list that represents the
multiple header string values. Leading and trailing whitespaces are
removed from all string values retrieved from the given map and its lists
before processing. Only headers that, after filtering, contain at least
one, possibly empty string, value will be added to the HTTP headers.

**API Note:** The primary purpose of this method is for testing frameworks.
Per-request headers can be set through one of the

HttpRequest

headers

methods.
**Parameters:** headerMap

- the map containing the header names and values
**Parameters:** filter

- a filter that can be used to inspect each
header-name-and-value pair in the given map to determine if
it should, or should not, be added to the to the HTTP
headers
**Returns:** an HTTP headers instance containing the given headers
**Throws:** NullPointerException

- if any of:

headerMap

, a key or value
in the given map, or an entry in the map's value list, or

filter

, is

null
**Throws:** IllegalArgumentException

- if the given

headerMap

contains
any two keys that are equal ( without regard to case ); or if the
given map contains any key whose length, after trimming
whitespaces, is

0

---

#### Method Detail

firstValue

```java
public
Optional
<
String
> firstValue​(
String
name)
```

Returns an

Optional

containing the first header string value of
the given named (and possibly multi-valued) header. If the header is not
present, then the returned

Optional

is empty.

**Parameters:** name

- the header name
**Returns:** an

Optional<String>

containing the first named header
string value, if present

---

#### firstValue

public

Optional

<

String

> firstValue​(

String

name)

Returns an

Optional

containing the first header string value of
the given named (and possibly multi-valued) header. If the header is not
present, then the returned

Optional

is empty.

firstValueAsLong

```java
public
OptionalLong
firstValueAsLong​(
String
name)
```

Returns an

OptionalLong

containing the first header string value
of the named header field. If the header is not present, then the
Optional is empty. If the header is present but contains a value that
does not parse as a

Long

value, then an exception is thrown.

**Parameters:** name

- the header name
**Returns:** an

OptionalLong
**Throws:** NumberFormatException

- if a value is found, but does not parse as
a Long

---

#### firstValueAsLong

public

OptionalLong

firstValueAsLong​(

String

name)

Returns an

OptionalLong

containing the first header string value
of the named header field. If the header is not present, then the
Optional is empty. If the header is present but contains a value that
does not parse as a

Long

value, then an exception is thrown.

allValues

```java
public
List
<
String
> allValues​(
String
name)
```

Returns an unmodifiable List of all of the header string values of the
given named header. Always returns a List, which may be empty if the
header is not present.

**Parameters:** name

- the header name
**Returns:** a List of headers string values

---

#### allValues

public

List

<

String

> allValues​(

String

name)

Returns an unmodifiable List of all of the header string values of the
given named header. Always returns a List, which may be empty if the
header is not present.

map

```java
public
Map
<
String
,​
List
<
String
>> map()
```

Returns an unmodifiable multi Map view of this HttpHeaders.

**Returns:** the Map

---

#### map

public

Map

<

String

,​

List

<

String

>> map()

Returns an unmodifiable multi Map view of this HttpHeaders.

equals

```java
public final boolean equals​(
Object
obj)
```

Tests this HTTP headers instance for equality with the given object.

If the given object is not an

HttpHeaders

then this
method returns

false

. Two HTTP headers are equal if each
of their corresponding

maps

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is an

HttpHeaders

that is equal to this HTTP headers
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

obj)

Tests this HTTP headers instance for equality with the given object.

If the given object is not an

HttpHeaders

then this
method returns

false

. Two HTTP headers are equal if each
of their corresponding

maps

are equal.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not an

HttpHeaders

then this
method returns

false

. Two HTTP headers are equal if each
of their corresponding

maps

are equal.

This method satisfies the general contract of the

Object.equals

method.

This method satisfies the general contract of the

Object.equals

method.

hashCode

```java
public final int hashCode()
```

Computes a hash code for this HTTP headers instance.

The hash code is based upon the components of the HTTP headers

map

, and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** the hash-code value for this HTTP headers
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Computes a hash code for this HTTP headers instance.

The hash code is based upon the components of the HTTP headers

map

, and satisfies the general contract of the

Object.hashCode

method.

The hash code is based upon the components of the HTTP headers

map

, and satisfies the general contract of the

Object.hashCode

method.

toString

```java
public
String
toString()
```

Returns this HTTP headers as a string.

**Overrides:** toString

in class

Object
**Returns:** a string describing the HTTP headers

---

#### toString

public

String

toString()

Returns this HTTP headers as a string.

of

```java
public static
HttpHeaders
of​(
Map
<
String
,​
List
<
String
>> headerMap,

BiPredicate
<
String
,​
String
> filter)
```

Returns an HTTP headers from the given map. The given map's key
represents the header name, and its value the list of string header
values for that header name.

An HTTP header name may appear more than once in the HTTP protocol.
Such,

multi-valued

, headers must be represented by a single entry
in the given map, whose entry value is a list that represents the
multiple header string values. Leading and trailing whitespaces are
removed from all string values retrieved from the given map and its lists
before processing. Only headers that, after filtering, contain at least
one, possibly empty string, value will be added to the HTTP headers.

**API Note:** The primary purpose of this method is for testing frameworks.
Per-request headers can be set through one of the

HttpRequest

headers

methods.
**Parameters:** headerMap

- the map containing the header names and values
**Parameters:** filter

- a filter that can be used to inspect each
header-name-and-value pair in the given map to determine if
it should, or should not, be added to the to the HTTP
headers
**Returns:** an HTTP headers instance containing the given headers
**Throws:** NullPointerException

- if any of:

headerMap

, a key or value
in the given map, or an entry in the map's value list, or

filter

, is

null
**Throws:** IllegalArgumentException

- if the given

headerMap

contains
any two keys that are equal ( without regard to case ); or if the
given map contains any key whose length, after trimming
whitespaces, is

0

---

#### of

public static

HttpHeaders

of​(

Map

<

String

,​

List

<

String

>> headerMap,

BiPredicate

<

String

,​

String

> filter)

Returns an HTTP headers from the given map. The given map's key
represents the header name, and its value the list of string header
values for that header name.

An HTTP header name may appear more than once in the HTTP protocol.
Such,

multi-valued

, headers must be represented by a single entry
in the given map, whose entry value is a list that represents the
multiple header string values. Leading and trailing whitespaces are
removed from all string values retrieved from the given map and its lists
before processing. Only headers that, after filtering, contain at least
one, possibly empty string, value will be added to the HTTP headers.

An HTTP header name may appear more than once in the HTTP protocol.
Such,

multi-valued

, headers must be represented by a single entry
in the given map, whose entry value is a list that represents the
multiple header string values. Leading and trailing whitespaces are
removed from all string values retrieved from the given map and its lists
before processing. Only headers that, after filtering, contain at least
one, possibly empty string, value will be added to the HTTP headers.

---

