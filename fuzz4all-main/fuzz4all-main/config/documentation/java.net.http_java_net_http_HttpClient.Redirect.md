# Enum HttpClient.Redirect

**Source:** `java.net.http\java\net\http\HttpClient.Redirect.html`

### Class Description

```java
public static enum
HttpClient.Redirect

extends
Enum
<
HttpClient.Redirect
>
```

Defines the automatic redirection policy.

The automatic redirection policy is checked whenever a

3XX

response code is received. If redirection does not happen automatically,
then the response, containing the

3XX

response code, is returned,
where it can be handled manually.

Redirect

policy is set through the

Builder.followRedirects

method.

**All Implemented Interfaces:** Serializable

,

Comparable

<

HttpClient.Redirect

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
HttpClient.Redirect
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HttpClient.Redirect c : HttpClient.Redirect.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
HttpClient.Redirect
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum HttpClient.Redirect

java.lang.Object

- java.lang.Enum

<

HttpClient.Redirect

>
- - java.net.http.HttpClient.Redirect

java.lang.Enum

<

HttpClient.Redirect

>

- java.net.http.HttpClient.Redirect

java.net.http.HttpClient.Redirect

**All Implemented Interfaces:** Serializable

,

Comparable

<

HttpClient.Redirect

>

**Enclosing class:** HttpClient

```java
public static enum
HttpClient.Redirect

extends
Enum
<
HttpClient.Redirect
>
```

Defines the automatic redirection policy.

The automatic redirection policy is checked whenever a

3XX

response code is received. If redirection does not happen automatically,
then the response, containing the

3XX

response code, is returned,
where it can be handled manually.

Redirect

policy is set through the

Builder.followRedirects

method.

**Implementation Note:** When automatic redirection occurs, the request method of the
redirected request may be modified depending on the specific

30X

status code, as specified in

RFC 7231

. In addition, the

301

and

302

status codes
cause a

POST

request to be converted to a

GET

in the
redirected request.
**Since:** 11

public static enum

HttpClient.Redirect

extends

Enum

<

HttpClient.Redirect

>

Defines the automatic redirection policy.

The automatic redirection policy is checked whenever a

3XX

response code is received. If redirection does not happen automatically,
then the response, containing the

3XX

response code, is returned,
where it can be handled manually.

Redirect

policy is set through the

Builder.followRedirects

method.

The automatic redirection policy is checked whenever a

3XX

response code is received. If redirection does not happen automatically,
then the response, containing the

3XX

response code, is returned,
where it can be handled manually.

Redirect

policy is set through the

Builder.followRedirects

method.

Redirect

policy is set through the

Builder.followRedirects

method.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ALWAYS

Always redirect.

NEVER

Never redirect.

NORMAL

Always redirect, except from HTTPS URLs to HTTP URLs.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

HttpClient.Redirect

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

HttpClient.Redirect

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

ALWAYS

Always redirect.

NEVER

Never redirect.

NORMAL

Always redirect, except from HTTPS URLs to HTTP URLs.

---

#### Enum Constant Summary

Always redirect.

Never redirect.

Always redirect, except from HTTPS URLs to HTTP URLs.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

HttpClient.Redirect

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

HttpClient.Redirect

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- NEVER

```java
public static final
HttpClient.Redirect
NEVER
```

Never redirect.

- ALWAYS

```java
public static final
HttpClient.Redirect
ALWAYS
```

Always redirect.

- NORMAL

```java
public static final
HttpClient.Redirect
NORMAL
```

Always redirect, except from HTTPS URLs to HTTP URLs.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
HttpClient.Redirect
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HttpClient.Redirect c : HttpClient.Redirect.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
HttpClient.Redirect
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- NEVER

```java
public static final
HttpClient.Redirect
NEVER
```

Never redirect.

- ALWAYS

```java
public static final
HttpClient.Redirect
ALWAYS
```

Always redirect.

- NORMAL

```java
public static final
HttpClient.Redirect
NORMAL
```

Always redirect, except from HTTPS URLs to HTTP URLs.

---

#### Enum Constant Detail

NEVER

```java
public static final
HttpClient.Redirect
NEVER
```

Never redirect.

---

#### NEVER

public static final

HttpClient.Redirect

NEVER

Never redirect.

ALWAYS

```java
public static final
HttpClient.Redirect
ALWAYS
```

Always redirect.

---

#### ALWAYS

public static final

HttpClient.Redirect

ALWAYS

Always redirect.

NORMAL

```java
public static final
HttpClient.Redirect
NORMAL
```

Always redirect, except from HTTPS URLs to HTTP URLs.

---

#### NORMAL

public static final

HttpClient.Redirect

NORMAL

Always redirect, except from HTTPS URLs to HTTP URLs.

Method Detail

- values

```java
public static
HttpClient.Redirect
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HttpClient.Redirect c : HttpClient.Redirect.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
HttpClient.Redirect
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
HttpClient.Redirect
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HttpClient.Redirect c : HttpClient.Redirect.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

HttpClient.Redirect

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (HttpClient.Redirect c : HttpClient.Redirect.values())
System.out.println(c);
```

for (HttpClient.Redirect c : HttpClient.Redirect.values())
System.out.println(c);

valueOf

```java
public static
HttpClient.Redirect
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

HttpClient.Redirect

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

