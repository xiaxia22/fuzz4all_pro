# Class Headers

**Source:** `jdk.httpserver\com\sun\net\httpserver\Headers.html`

### Class Description

```java
public class
Headers

extends
Object

implements
Map
<
String
,​
List
<
String
>>
```

HTTP request and response headers are represented by this class which implements
the interface

Map

<

String

,

List

<

String

>>.
The keys are case-insensitive Strings representing the header names and
the value associated with each key is
a

List

<

String

> with one
element for each occurrence of the header name in the request or response.

For example, if a response header instance contains
one key "HeaderName" with two values "value1 and value2"
then this object is output as two header lines:

```java
HeaderName: value1
HeaderName: value2
```

All the normal

Map

methods are provided, but the following
additional convenience methods are most likely to be used:

- getFirst(String)

returns a single valued header or the first value of
a multi-valued header.
- add(String,String)

adds the given header value to the list for the given key
- set(String,String)

sets the given header field to the single value given
overwriting any existing values in the value list.

All methods in this class accept

null

values for keys and values. However, null
keys will never will be present in HTTP request headers, and will not be output/sent in response headers.
Null values can be represented as either a null entry for the key (i.e. the list is null) or
where the key has a list, but one (or more) of the list's values is null. Null values are output
as a header line containing the key but no associated value.

**All Implemented Interfaces:** Map

<

String

,​

List

<

String

>>

---

### Field Details

*No entries found.*

### Constructor Details

#### public Headers()

*No description found.*

---

### Method Details

#### public
String
getFirst​(
String
key)

returns the first value from the List of String values
for the given key (if at least one exists).

**Parameters:**
- key

- the key to search for

**Returns:**
- the first string value associated with the key

---

#### public void add​(
String
key,

String
value)

adds the given value to the list of headers
for the given key. If the mapping does not
already exist, then it is created

**Parameters:**
- key

- the header name
- value

- the header value to add to the header

---

#### public void set​(
String
key,

String
value)

sets the given value as the sole header value
for the given key. If the mapping does not
already exist, then it is created

**Parameters:**
- key

- the header name
- value

- the header value to set.

---

### Additional Sections

#### Class Headers

java.lang.Object

- com.sun.net.httpserver.Headers

com.sun.net.httpserver.Headers

**All Implemented Interfaces:** Map

<

String

,​

List

<

String

>>

```java
public class
Headers

extends
Object

implements
Map
<
String
,​
List
<
String
>>
```

HTTP request and response headers are represented by this class which implements
the interface

Map

<

String

,

List

<

String

>>.
The keys are case-insensitive Strings representing the header names and
the value associated with each key is
a

List

<

String

> with one
element for each occurrence of the header name in the request or response.

For example, if a response header instance contains
one key "HeaderName" with two values "value1 and value2"
then this object is output as two header lines:

```java
HeaderName: value1
HeaderName: value2
```

All the normal

Map

methods are provided, but the following
additional convenience methods are most likely to be used:

- getFirst(String)

returns a single valued header or the first value of
a multi-valued header.
- add(String,String)

adds the given header value to the list for the given key
- set(String,String)

sets the given header field to the single value given
overwriting any existing values in the value list.

All methods in this class accept

null

values for keys and values. However, null
keys will never will be present in HTTP request headers, and will not be output/sent in response headers.
Null values can be represented as either a null entry for the key (i.e. the list is null) or
where the key has a list, but one (or more) of the list's values is null. Null values are output
as a header line containing the key but no associated value.

**Since:** 1.6

public class

Headers

extends

Object

implements

Map

<

String

,​

List

<

String

>>

HTTP request and response headers are represented by this class which implements
the interface

Map

<

String

,

List

<

String

>>.
The keys are case-insensitive Strings representing the header names and
the value associated with each key is
a

List

<

String

> with one
element for each occurrence of the header name in the request or response.

For example, if a response header instance contains
one key "HeaderName" with two values "value1 and value2"
then this object is output as two header lines:

```java
HeaderName: value1
HeaderName: value2
```

All the normal

Map

methods are provided, but the following
additional convenience methods are most likely to be used:

- getFirst(String)

returns a single valued header or the first value of
a multi-valued header.
- add(String,String)

adds the given header value to the list for the given key
- set(String,String)

sets the given header field to the single value given
overwriting any existing values in the value list.

All methods in this class accept

null

values for keys and values. However, null
keys will never will be present in HTTP request headers, and will not be output/sent in response headers.
Null values can be represented as either a null entry for the key (i.e. the list is null) or
where the key has a list, but one (or more) of the list's values is null. Null values are output
as a header line containing the key but no associated value.

For example, if a response header instance contains
one key "HeaderName" with two values "value1 and value2"
then this object is output as two header lines:

```java
HeaderName: value1
HeaderName: value2
```

All the normal

Map

methods are provided, but the following
additional convenience methods are most likely to be used:

- getFirst(String)

returns a single valued header or the first value of
a multi-valued header.
- add(String,String)

adds the given header value to the list for the given key
- set(String,String)

sets the given header field to the single value given
overwriting any existing values in the value list.

All methods in this class accept

null

values for keys and values. However, null
keys will never will be present in HTTP request headers, and will not be output/sent in response headers.
Null values can be represented as either a null entry for the key (i.e. the list is null) or
where the key has a list, but one (or more) of the list's values is null. Null values are output
as a header line containing the key but no associated value.

HeaderName: value1
HeaderName: value2

All the normal

Map

methods are provided, but the following
additional convenience methods are most likely to be used:

- getFirst(String)

returns a single valued header or the first value of
a multi-valued header.
- add(String,String)

adds the given header value to the list for the given key
- set(String,String)

sets the given header field to the single value given
overwriting any existing values in the value list.

All methods in this class accept

null

values for keys and values. However, null
keys will never will be present in HTTP request headers, and will not be output/sent in response headers.
Null values can be represented as either a null entry for the key (i.e. the list is null) or
where the key has a list, but one (or more) of the list's values is null. Null values are output
as a header line containing the key but no associated value.

getFirst(String)

returns a single valued header or the first value of
a multi-valued header.

add(String,String)

adds the given header value to the list for the given key

set(String,String)

sets the given header field to the single value given
overwriting any existing values in the value list.

All methods in this class accept

null

values for keys and values. However, null
keys will never will be present in HTTP request headers, and will not be output/sent in response headers.
Null values can be represented as either a null entry for the key (i.e. the list is null) or
where the key has a list, but one (or more) of the list's values is null. Null values are output
as a header line containing the key but no associated value.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Headers

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(

String

key,

String

value)

adds the given value to the list of headers
for the given key.

String

getFirst

​(

String

key)

returns the first value from the List of String values
for the given key (if at least one exists).

void

set

​(

String

key,

String

value)

sets the given value as the sole header value
for the given key.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.util.

Map

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

containsKey

,

containsValue

,

entrySet

,

equals

,

forEach

,

get

,

getOrDefault

,

hashCode

,

isEmpty

,

keySet

,

merge

,

put

,

putAll

,

putIfAbsent

,

remove

,

remove

,

replace

,

replace

,

replaceAll

,

size

,

values

Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

---

#### Nested Class Summary

Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

---

#### Nested classes/interfaces declared in interface java.util. Map

Constructor Summary

Constructors

Constructor

Description

Headers

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(

String

key,

String

value)

adds the given value to the list of headers
for the given key.

String

getFirst

​(

String

key)

returns the first value from the List of String values
for the given key (if at least one exists).

void

set

​(

String

key,

String

value)

sets the given value as the sole header value
for the given key.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.util.

Map

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

containsKey

,

containsValue

,

entrySet

,

equals

,

forEach

,

get

,

getOrDefault

,

hashCode

,

isEmpty

,

keySet

,

merge

,

put

,

putAll

,

putIfAbsent

,

remove

,

remove

,

replace

,

replace

,

replaceAll

,

size

,

values

---

#### Method Summary

adds the given value to the list of headers
for the given key.

returns the first value from the List of String values
for the given key (if at least one exists).

sets the given value as the sole header value
for the given key.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.util.

Map

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

containsKey

,

containsValue

,

entrySet

,

equals

,

forEach

,

get

,

getOrDefault

,

hashCode

,

isEmpty

,

keySet

,

merge

,

put

,

putAll

,

putIfAbsent

,

remove

,

remove

,

replace

,

replace

,

replaceAll

,

size

,

values

---

#### Methods declared in interface java.util. Map

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Headers

```java
public Headers()
```

============ METHOD DETAIL ==========

- Method Detail

- getFirst

```java
public
String
getFirst​(
String
key)
```

returns the first value from the List of String values
for the given key (if at least one exists).

**Parameters:** key

- the key to search for
**Returns:** the first string value associated with the key

- add

```java
public void add​(
String
key,

String
value)
```

adds the given value to the list of headers
for the given key. If the mapping does not
already exist, then it is created

**Parameters:** key

- the header name
**Parameters:** value

- the header value to add to the header

- set

```java
public void set​(
String
key,

String
value)
```

sets the given value as the sole header value
for the given key. If the mapping does not
already exist, then it is created

**Parameters:** key

- the header name
**Parameters:** value

- the header value to set.

Constructor Detail

- Headers

```java
public Headers()
```

---

#### Constructor Detail

Headers

```java
public Headers()
```

---

#### Headers

public Headers()

Method Detail

- getFirst

```java
public
String
getFirst​(
String
key)
```

returns the first value from the List of String values
for the given key (if at least one exists).

**Parameters:** key

- the key to search for
**Returns:** the first string value associated with the key

- add

```java
public void add​(
String
key,

String
value)
```

adds the given value to the list of headers
for the given key. If the mapping does not
already exist, then it is created

**Parameters:** key

- the header name
**Parameters:** value

- the header value to add to the header

- set

```java
public void set​(
String
key,

String
value)
```

sets the given value as the sole header value
for the given key. If the mapping does not
already exist, then it is created

**Parameters:** key

- the header name
**Parameters:** value

- the header value to set.

---

#### Method Detail

getFirst

```java
public
String
getFirst​(
String
key)
```

returns the first value from the List of String values
for the given key (if at least one exists).

**Parameters:** key

- the key to search for
**Returns:** the first string value associated with the key

---

#### getFirst

public

String

getFirst​(

String

key)

returns the first value from the List of String values
for the given key (if at least one exists).

add

```java
public void add​(
String
key,

String
value)
```

adds the given value to the list of headers
for the given key. If the mapping does not
already exist, then it is created

**Parameters:** key

- the header name
**Parameters:** value

- the header value to add to the header

---

#### add

public void add​(

String

key,

String

value)

adds the given value to the list of headers
for the given key. If the mapping does not
already exist, then it is created

set

```java
public void set​(
String
key,

String
value)
```

sets the given value as the sole header value
for the given key. If the mapping does not
already exist, then it is created

**Parameters:** key

- the header name
**Parameters:** value

- the header value to set.

---

#### set

public void set​(

String

key,

String

value)

sets the given value as the sole header value
for the given key. If the mapping does not
already exist, then it is created

---

