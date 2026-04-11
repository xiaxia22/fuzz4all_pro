# Class URLEncoder

**Source:** `java.base\java\net\URLEncoder.html`

### Class Description

```java
public class
URLEncoder

extends
Object
```

Utility class for HTML form encoding. This class contains static methods
for converting a String to the

application/x-www-form-urlencoded

MIME
format. For more information about HTML form encoding, consult the HTML

specification

.

When encoding a String, the following rules apply:

- The alphanumeric characters "

a

" through
"

z

", "

A

" through
"

Z

" and "

0

"
through "

9

" remain the same.

The special characters "

.

",
"

-

", "

*

", and
"

_

" remain the same.

The space character " " is
converted into a plus sign "

+

".

All other characters are unsafe and are first converted into
one or more bytes using some encoding scheme. Then each byte is
represented by the 3-character string
"

%xy

", where

xy

is the
two-digit hexadecimal representation of the byte.
The recommended encoding scheme to use is UTF-8. However,
for compatibility reasons, if an encoding is not specified,
then the default encoding of the platform is used.

For example using UTF-8 as the encoding scheme the string "The
string ü@foo-bar" would get converted to
"The+string+%C3%BC%40foo-bar" because in UTF-8 the character
ü is encoded as two bytes C3 (hex) and BC (hex), and the
character @ is encoded as one byte 40 (hex).

**Since:** 1.0

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### @Deprecated

public static
String
encode​(
String
s)

Translates a string into

x-www-form-urlencoded

format. This method uses the platform's default encoding
as the encoding scheme to obtain the bytes for unsafe characters.

**Parameters:**
- s

-

String

to be translated.

**Returns:**
- the translated

String

.

---

#### public static
String
encode​(
String
s,

String
enc)
throws
UnsupportedEncodingException

Translates a string into

application/x-www-form-urlencoded

format using a specific encoding scheme.

This method behaves the same as

encode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

**Parameters:**
- s

-

String

to be translated.
- enc

- The name of a supported

character
encoding

.

**Returns:**
- the translated

String

.

**Throws:**
- UnsupportedEncodingException

- If the named encoding is not supported

**See Also:**
- URLDecoder.decode(java.lang.String, java.lang.String)

**Since:**
- 1.4

---

#### public static
String
encode​(
String
s,

Charset
charset)

Translates a string into

application/x-www-form-urlencoded

format using a specific

Charset

.
This method uses the supplied charset to obtain the bytes for unsafe
characters.

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce incompatibilities.

**Parameters:**
- s

-

String

to be translated.
- charset

- the given charset

**Returns:**
- the translated

String

.

**Throws:**
- NullPointerException

- if

s

or

charset

is

null

.

**See Also:**
- URLDecoder.decode(java.lang.String, java.nio.charset.Charset)

**Since:**
- 10

---

### Additional Sections

#### Class URLEncoder

java.lang.Object

- java.net.URLEncoder

java.net.URLEncoder

```java
public class
URLEncoder

extends
Object
```

Utility class for HTML form encoding. This class contains static methods
for converting a String to the

application/x-www-form-urlencoded

MIME
format. For more information about HTML form encoding, consult the HTML

specification

.

When encoding a String, the following rules apply:

- The alphanumeric characters "

a

" through
"

z

", "

A

" through
"

Z

" and "

0

"
through "

9

" remain the same.

The special characters "

.

",
"

-

", "

*

", and
"

_

" remain the same.

The space character " " is
converted into a plus sign "

+

".

All other characters are unsafe and are first converted into
one or more bytes using some encoding scheme. Then each byte is
represented by the 3-character string
"

%xy

", where

xy

is the
two-digit hexadecimal representation of the byte.
The recommended encoding scheme to use is UTF-8. However,
for compatibility reasons, if an encoding is not specified,
then the default encoding of the platform is used.

For example using UTF-8 as the encoding scheme the string "The
string ü@foo-bar" would get converted to
"The+string+%C3%BC%40foo-bar" because in UTF-8 the character
ü is encoded as two bytes C3 (hex) and BC (hex), and the
character @ is encoded as one byte 40 (hex).

**Since:** 1.0

public class

URLEncoder

extends

Object

Utility class for HTML form encoding. This class contains static methods
for converting a String to the

application/x-www-form-urlencoded

MIME
format. For more information about HTML form encoding, consult the HTML

specification

.

When encoding a String, the following rules apply:

- The alphanumeric characters "

a

" through
"

z

", "

A

" through
"

Z

" and "

0

"
through "

9

" remain the same.

The special characters "

.

",
"

-

", "

*

", and
"

_

" remain the same.

The space character " " is
converted into a plus sign "

+

".

All other characters are unsafe and are first converted into
one or more bytes using some encoding scheme. Then each byte is
represented by the 3-character string
"

%xy

", where

xy

is the
two-digit hexadecimal representation of the byte.
The recommended encoding scheme to use is UTF-8. However,
for compatibility reasons, if an encoding is not specified,
then the default encoding of the platform is used.

For example using UTF-8 as the encoding scheme the string "The
string ü@foo-bar" would get converted to
"The+string+%C3%BC%40foo-bar" because in UTF-8 the character
ü is encoded as two bytes C3 (hex) and BC (hex), and the
character @ is encoded as one byte 40 (hex).

When encoding a String, the following rules apply:

- The alphanumeric characters "

a

" through
"

z

", "

A

" through
"

Z

" and "

0

"
through "

9

" remain the same.

The special characters "

.

",
"

-

", "

*

", and
"

_

" remain the same.

The space character " " is
converted into a plus sign "

+

".

All other characters are unsafe and are first converted into
one or more bytes using some encoding scheme. Then each byte is
represented by the 3-character string
"

%xy

", where

xy

is the
two-digit hexadecimal representation of the byte.
The recommended encoding scheme to use is UTF-8. However,
for compatibility reasons, if an encoding is not specified,
then the default encoding of the platform is used.

For example using UTF-8 as the encoding scheme the string "The
string ü@foo-bar" would get converted to
"The+string+%C3%BC%40foo-bar" because in UTF-8 the character
ü is encoded as two bytes C3 (hex) and BC (hex), and the
character @ is encoded as one byte 40 (hex).

The alphanumeric characters "

a

" through
"

z

", "

A

" through
"

Z

" and "

0

"
through "

9

" remain the same.

The special characters "

.

",
"

-

", "

*

", and
"

_

" remain the same.

The space character " " is
converted into a plus sign "

+

".

All other characters are unsafe and are first converted into
one or more bytes using some encoding scheme. Then each byte is
represented by the 3-character string
"

%xy

", where

xy

is the
two-digit hexadecimal representation of the byte.
The recommended encoding scheme to use is UTF-8. However,
for compatibility reasons, if an encoding is not specified,
then the default encoding of the platform is used.

For example using UTF-8 as the encoding scheme the string "The
string ü@foo-bar" would get converted to
"The+string+%C3%BC%40foo-bar" because in UTF-8 the character
ü is encoded as two bytes C3 (hex) and BC (hex), and the
character @ is encoded as one byte 40 (hex).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

String

encode

​(

String

s)

Deprecated.

The resulting string may vary depending on the platform's
default encoding.

static

String

encode

​(

String

s,

String

enc)

Translates a string into

application/x-www-form-urlencoded

format using a specific encoding scheme.

static

String

encode

​(

String

s,

Charset

charset)

Translates a string into

application/x-www-form-urlencoded

format using a specific

Charset

.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

String

encode

​(

String

s)

Deprecated.

The resulting string may vary depending on the platform's
default encoding.

static

String

encode

​(

String

s,

String

enc)

Translates a string into

application/x-www-form-urlencoded

format using a specific encoding scheme.

static

String

encode

​(

String

s,

Charset

charset)

Translates a string into

application/x-www-form-urlencoded

format using a specific

Charset

.

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

---

#### Method Summary

Deprecated.

The resulting string may vary depending on the platform's
default encoding.

Translates a string into

application/x-www-form-urlencoded

format using a specific encoding scheme.

Translates a string into

application/x-www-form-urlencoded

format using a specific

Charset

.

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

============ METHOD DETAIL ==========

- Method Detail

- encode

```java
@Deprecated

public static
String
encode​(
String
s)
```

Deprecated.

The resulting string may vary depending on the platform's
default encoding. Instead, use the encode(String,String)
method to specify the encoding.

Translates a string into

x-www-form-urlencoded

format. This method uses the platform's default encoding
as the encoding scheme to obtain the bytes for unsafe characters.

**Parameters:** s

-

String

to be translated.
**Returns:** the translated

String

.

- encode

```java
public static
String
encode​(
String
s,

String
enc)
throws
UnsupportedEncodingException
```

Translates a string into

application/x-www-form-urlencoded

format using a specific encoding scheme.

This method behaves the same as

encode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

**Parameters:** s

-

String

to be translated.
**Parameters:** enc

- The name of a supported

character
encoding

.
**Returns:** the translated

String

.
**Throws:** UnsupportedEncodingException

- If the named encoding is not supported
**Since:** 1.4
**See Also:** URLDecoder.decode(java.lang.String, java.lang.String)

- encode

```java
public static
String
encode​(
String
s,

Charset
charset)
```

Translates a string into

application/x-www-form-urlencoded

format using a specific

Charset

.
This method uses the supplied charset to obtain the bytes for unsafe
characters.

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce incompatibilities.

**Parameters:** s

-

String

to be translated.
**Parameters:** charset

- the given charset
**Returns:** the translated

String

.
**Throws:** NullPointerException

- if

s

or

charset

is

null

.
**Since:** 10
**See Also:** URLDecoder.decode(java.lang.String, java.nio.charset.Charset)

Method Detail

- encode

```java
@Deprecated

public static
String
encode​(
String
s)
```

Deprecated.

The resulting string may vary depending on the platform's
default encoding. Instead, use the encode(String,String)
method to specify the encoding.

Translates a string into

x-www-form-urlencoded

format. This method uses the platform's default encoding
as the encoding scheme to obtain the bytes for unsafe characters.

**Parameters:** s

-

String

to be translated.
**Returns:** the translated

String

.

- encode

```java
public static
String
encode​(
String
s,

String
enc)
throws
UnsupportedEncodingException
```

Translates a string into

application/x-www-form-urlencoded

format using a specific encoding scheme.

This method behaves the same as

encode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

**Parameters:** s

-

String

to be translated.
**Parameters:** enc

- The name of a supported

character
encoding

.
**Returns:** the translated

String

.
**Throws:** UnsupportedEncodingException

- If the named encoding is not supported
**Since:** 1.4
**See Also:** URLDecoder.decode(java.lang.String, java.lang.String)

- encode

```java
public static
String
encode​(
String
s,

Charset
charset)
```

Translates a string into

application/x-www-form-urlencoded

format using a specific

Charset

.
This method uses the supplied charset to obtain the bytes for unsafe
characters.

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce incompatibilities.

**Parameters:** s

-

String

to be translated.
**Parameters:** charset

- the given charset
**Returns:** the translated

String

.
**Throws:** NullPointerException

- if

s

or

charset

is

null

.
**Since:** 10
**See Also:** URLDecoder.decode(java.lang.String, java.nio.charset.Charset)

---

#### Method Detail

encode

```java
@Deprecated

public static
String
encode​(
String
s)
```

Deprecated.

The resulting string may vary depending on the platform's
default encoding. Instead, use the encode(String,String)
method to specify the encoding.

Translates a string into

x-www-form-urlencoded

format. This method uses the platform's default encoding
as the encoding scheme to obtain the bytes for unsafe characters.

**Parameters:** s

-

String

to be translated.
**Returns:** the translated

String

.

---

#### encode

@Deprecated

public static

String

encode​(

String

s)

Translates a string into

x-www-form-urlencoded

format. This method uses the platform's default encoding
as the encoding scheme to obtain the bytes for unsafe characters.

encode

```java
public static
String
encode​(
String
s,

String
enc)
throws
UnsupportedEncodingException
```

Translates a string into

application/x-www-form-urlencoded

format using a specific encoding scheme.

This method behaves the same as

encode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

**Parameters:** s

-

String

to be translated.
**Parameters:** enc

- The name of a supported

character
encoding

.
**Returns:** the translated

String

.
**Throws:** UnsupportedEncodingException

- If the named encoding is not supported
**Since:** 1.4
**See Also:** URLDecoder.decode(java.lang.String, java.lang.String)

---

#### encode

public static

String

encode​(

String

s,

String

enc)
throws

UnsupportedEncodingException

Translates a string into

application/x-www-form-urlencoded

format using a specific encoding scheme.

This method behaves the same as

encode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

This method behaves the same as

encode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

encode

```java
public static
String
encode​(
String
s,

Charset
charset)
```

Translates a string into

application/x-www-form-urlencoded

format using a specific

Charset

.
This method uses the supplied charset to obtain the bytes for unsafe
characters.

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce incompatibilities.

**Parameters:** s

-

String

to be translated.
**Parameters:** charset

- the given charset
**Returns:** the translated

String

.
**Throws:** NullPointerException

- if

s

or

charset

is

null

.
**Since:** 10
**See Also:** URLDecoder.decode(java.lang.String, java.nio.charset.Charset)

---

#### encode

public static

String

encode​(

String

s,

Charset

charset)

Translates a string into

application/x-www-form-urlencoded

format using a specific

Charset

.
This method uses the supplied charset to obtain the bytes for unsafe
characters.

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce incompatibilities.

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce incompatibilities.

---

