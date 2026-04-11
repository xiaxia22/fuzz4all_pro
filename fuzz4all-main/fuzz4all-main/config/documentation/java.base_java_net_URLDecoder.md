# Class URLDecoder

**Source:** `java.base\java\net\URLDecoder.html`

### Class Description

```java
public class
URLDecoder

extends
Object
```

Utility class for HTML form decoding. This class contains static methods
for decoding a String from the

application/x-www-form-urlencoded

MIME format.

The conversion process is the reverse of that used by the URLEncoder class. It is assumed
that all characters in the encoded string are one of the following:
"

a

" through "

z

",
"

A

" through "

Z

",
"

0

" through "

9

", and
"

-

", "

_

",
"

.

", and "

*

". The
character "

%

" is allowed but is interpreted
as the start of a special escaped sequence.

The following rules are applied in the conversion:

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

The plus sign "

+

" is converted into a
space character " " .

A sequence of the form "

%xy

" will be
treated as representing a byte where

xy

is the two-digit
hexadecimal representation of the 8 bits. Then, all substrings
that contain one or more of these byte sequences consecutively
will be replaced by the character(s) whose encoding would result
in those consecutive bytes.
The encoding scheme used to decode these characters may be specified,
or if unspecified, the default encoding of the platform will be used.

There are two possible ways in which this decoder could deal with
illegal strings. It could either leave illegal characters alone or
it could throw an

IllegalArgumentException

.
Which approach the decoder takes is left to the
implementation.

**Since:** 1.2

---

### Field Details

*No entries found.*

### Constructor Details

#### public URLDecoder()

*No description found.*

---

### Method Details

#### @Deprecated

public static
String
decode​(
String
s)

Decodes a

x-www-form-urlencoded

string.
The platform's default encoding is used to determine what characters
are represented by any consecutive sequences of the form
"

%xy

".

**Parameters:**
- s

- the

String

to decode

**Returns:**
- the newly decoded

String

---

#### public static
String
decode​(
String
s,

String
enc)
throws
UnsupportedEncodingException

Decodes an

application/x-www-form-urlencoded

string using
a specific encoding scheme.

This method behaves the same as

decode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

**Parameters:**
- s

- the

String

to decode
- enc

- The name of a supported

character
encoding

.

**Returns:**
- the newly decoded

String

**Throws:**
- UnsupportedEncodingException

- If character encoding needs to be consulted, but
named character encoding is not supported

**See Also:**
- URLEncoder.encode(java.lang.String, java.lang.String)

**Since:**
- 1.4

**Implementation Note:**
- This implementation will throw an

IllegalArgumentException

when illegal strings are encountered.

---

#### public static
String
decode​(
String
s,

Charset
charset)

Decodes an

application/x-www-form-urlencoded

string using
a specific

Charset

.
The supplied charset is used to determine
what characters are represented by any consecutive sequences of the
form "

%xy

".

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce
incompatibilities.

**Parameters:**
- s

- the

String

to decode
- charset

- the given charset

**Returns:**
- the newly decoded

String

**Throws:**
- NullPointerException

- if

s

or

charset

is

null
- IllegalArgumentException

- if the implementation encounters illegal
characters

**See Also:**
- URLEncoder.encode(java.lang.String, java.nio.charset.Charset)

**Since:**
- 10

**Implementation Note:**
- This implementation will throw an

IllegalArgumentException

when illegal strings are encountered.

---

### Additional Sections

#### Class URLDecoder

java.lang.Object

- java.net.URLDecoder

java.net.URLDecoder

```java
public class
URLDecoder

extends
Object
```

Utility class for HTML form decoding. This class contains static methods
for decoding a String from the

application/x-www-form-urlencoded

MIME format.

The conversion process is the reverse of that used by the URLEncoder class. It is assumed
that all characters in the encoded string are one of the following:
"

a

" through "

z

",
"

A

" through "

Z

",
"

0

" through "

9

", and
"

-

", "

_

",
"

.

", and "

*

". The
character "

%

" is allowed but is interpreted
as the start of a special escaped sequence.

The following rules are applied in the conversion:

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

The plus sign "

+

" is converted into a
space character " " .

A sequence of the form "

%xy

" will be
treated as representing a byte where

xy

is the two-digit
hexadecimal representation of the 8 bits. Then, all substrings
that contain one or more of these byte sequences consecutively
will be replaced by the character(s) whose encoding would result
in those consecutive bytes.
The encoding scheme used to decode these characters may be specified,
or if unspecified, the default encoding of the platform will be used.

There are two possible ways in which this decoder could deal with
illegal strings. It could either leave illegal characters alone or
it could throw an

IllegalArgumentException

.
Which approach the decoder takes is left to the
implementation.

**Since:** 1.2

public class

URLDecoder

extends

Object

Utility class for HTML form decoding. This class contains static methods
for decoding a String from the

application/x-www-form-urlencoded

MIME format.

The conversion process is the reverse of that used by the URLEncoder class. It is assumed
that all characters in the encoded string are one of the following:
"

a

" through "

z

",
"

A

" through "

Z

",
"

0

" through "

9

", and
"

-

", "

_

",
"

.

", and "

*

". The
character "

%

" is allowed but is interpreted
as the start of a special escaped sequence.

The following rules are applied in the conversion:

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

The plus sign "

+

" is converted into a
space character " " .

A sequence of the form "

%xy

" will be
treated as representing a byte where

xy

is the two-digit
hexadecimal representation of the 8 bits. Then, all substrings
that contain one or more of these byte sequences consecutively
will be replaced by the character(s) whose encoding would result
in those consecutive bytes.
The encoding scheme used to decode these characters may be specified,
or if unspecified, the default encoding of the platform will be used.

There are two possible ways in which this decoder could deal with
illegal strings. It could either leave illegal characters alone or
it could throw an

IllegalArgumentException

.
Which approach the decoder takes is left to the
implementation.

The conversion process is the reverse of that used by the URLEncoder class. It is assumed
that all characters in the encoded string are one of the following:
"

a

" through "

z

",
"

A

" through "

Z

",
"

0

" through "

9

", and
"

-

", "

_

",
"

.

", and "

*

". The
character "

%

" is allowed but is interpreted
as the start of a special escaped sequence.

The following rules are applied in the conversion:

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

The plus sign "

+

" is converted into a
space character " " .

A sequence of the form "

%xy

" will be
treated as representing a byte where

xy

is the two-digit
hexadecimal representation of the 8 bits. Then, all substrings
that contain one or more of these byte sequences consecutively
will be replaced by the character(s) whose encoding would result
in those consecutive bytes.
The encoding scheme used to decode these characters may be specified,
or if unspecified, the default encoding of the platform will be used.

There are two possible ways in which this decoder could deal with
illegal strings. It could either leave illegal characters alone or
it could throw an

IllegalArgumentException

.
Which approach the decoder takes is left to the
implementation.

The following rules are applied in the conversion:

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

The plus sign "

+

" is converted into a
space character " " .

A sequence of the form "

%xy

" will be
treated as representing a byte where

xy

is the two-digit
hexadecimal representation of the 8 bits. Then, all substrings
that contain one or more of these byte sequences consecutively
will be replaced by the character(s) whose encoding would result
in those consecutive bytes.
The encoding scheme used to decode these characters may be specified,
or if unspecified, the default encoding of the platform will be used.

There are two possible ways in which this decoder could deal with
illegal strings. It could either leave illegal characters alone or
it could throw an

IllegalArgumentException

.
Which approach the decoder takes is left to the
implementation.

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

The plus sign "

+

" is converted into a
space character " " .

A sequence of the form "

%xy

" will be
treated as representing a byte where

xy

is the two-digit
hexadecimal representation of the 8 bits. Then, all substrings
that contain one or more of these byte sequences consecutively
will be replaced by the character(s) whose encoding would result
in those consecutive bytes.
The encoding scheme used to decode these characters may be specified,
or if unspecified, the default encoding of the platform will be used.

There are two possible ways in which this decoder could deal with
illegal strings. It could either leave illegal characters alone or
it could throw an

IllegalArgumentException

.
Which approach the decoder takes is left to the
implementation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

URLDecoder

()

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

decode

​(

String

s)

Deprecated.

The resulting string may vary depending on the platform's
default encoding.

static

String

decode

​(

String

s,

String

enc)

Decodes an

application/x-www-form-urlencoded

string using
a specific encoding scheme.

static

String

decode

​(

String

s,

Charset

charset)

Decodes an

application/x-www-form-urlencoded

string using
a specific

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

Constructor Summary

Constructors

Constructor

Description

URLDecoder

()

---

#### Constructor Summary

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

decode

​(

String

s)

Deprecated.

The resulting string may vary depending on the platform's
default encoding.

static

String

decode

​(

String

s,

String

enc)

Decodes an

application/x-www-form-urlencoded

string using
a specific encoding scheme.

static

String

decode

​(

String

s,

Charset

charset)

Decodes an

application/x-www-form-urlencoded

string using
a specific

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

Decodes an

application/x-www-form-urlencoded

string using
a specific encoding scheme.

Decodes an

application/x-www-form-urlencoded

string using
a specific

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- URLDecoder

```java
public URLDecoder()
```

============ METHOD DETAIL ==========

- Method Detail

- decode

```java
@Deprecated

public static
String
decode​(
String
s)
```

Deprecated.

The resulting string may vary depending on the platform's
default encoding. Instead, use the decode(String,String) method
to specify the encoding.

Decodes a

x-www-form-urlencoded

string.
The platform's default encoding is used to determine what characters
are represented by any consecutive sequences of the form
"

%xy

".

**Parameters:** s

- the

String

to decode
**Returns:** the newly decoded

String

- decode

```java
public static
String
decode​(
String
s,

String
enc)
throws
UnsupportedEncodingException
```

Decodes an

application/x-www-form-urlencoded

string using
a specific encoding scheme.

This method behaves the same as

decode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

**Implementation Note:** This implementation will throw an

IllegalArgumentException

when illegal strings are encountered.
**Parameters:** s

- the

String

to decode
**Parameters:** enc

- The name of a supported

character
encoding

.
**Returns:** the newly decoded

String
**Throws:** UnsupportedEncodingException

- If character encoding needs to be consulted, but
named character encoding is not supported
**Since:** 1.4
**See Also:** URLEncoder.encode(java.lang.String, java.lang.String)

- decode

```java
public static
String
decode​(
String
s,

Charset
charset)
```

Decodes an

application/x-www-form-urlencoded

string using
a specific

Charset

.
The supplied charset is used to determine
what characters are represented by any consecutive sequences of the
form "

%xy

".

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce
incompatibilities.

**Implementation Note:** This implementation will throw an

IllegalArgumentException

when illegal strings are encountered.
**Parameters:** s

- the

String

to decode
**Parameters:** charset

- the given charset
**Returns:** the newly decoded

String
**Throws:** NullPointerException

- if

s

or

charset

is

null
**Throws:** IllegalArgumentException

- if the implementation encounters illegal
characters
**Since:** 10
**See Also:** URLEncoder.encode(java.lang.String, java.nio.charset.Charset)

Constructor Detail

- URLDecoder

```java
public URLDecoder()
```

---

#### Constructor Detail

URLDecoder

```java
public URLDecoder()
```

---

#### URLDecoder

public URLDecoder()

Method Detail

- decode

```java
@Deprecated

public static
String
decode​(
String
s)
```

Deprecated.

The resulting string may vary depending on the platform's
default encoding. Instead, use the decode(String,String) method
to specify the encoding.

Decodes a

x-www-form-urlencoded

string.
The platform's default encoding is used to determine what characters
are represented by any consecutive sequences of the form
"

%xy

".

**Parameters:** s

- the

String

to decode
**Returns:** the newly decoded

String

- decode

```java
public static
String
decode​(
String
s,

String
enc)
throws
UnsupportedEncodingException
```

Decodes an

application/x-www-form-urlencoded

string using
a specific encoding scheme.

This method behaves the same as

decode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

**Implementation Note:** This implementation will throw an

IllegalArgumentException

when illegal strings are encountered.
**Parameters:** s

- the

String

to decode
**Parameters:** enc

- The name of a supported

character
encoding

.
**Returns:** the newly decoded

String
**Throws:** UnsupportedEncodingException

- If character encoding needs to be consulted, but
named character encoding is not supported
**Since:** 1.4
**See Also:** URLEncoder.encode(java.lang.String, java.lang.String)

- decode

```java
public static
String
decode​(
String
s,

Charset
charset)
```

Decodes an

application/x-www-form-urlencoded

string using
a specific

Charset

.
The supplied charset is used to determine
what characters are represented by any consecutive sequences of the
form "

%xy

".

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce
incompatibilities.

**Implementation Note:** This implementation will throw an

IllegalArgumentException

when illegal strings are encountered.
**Parameters:** s

- the

String

to decode
**Parameters:** charset

- the given charset
**Returns:** the newly decoded

String
**Throws:** NullPointerException

- if

s

or

charset

is

null
**Throws:** IllegalArgumentException

- if the implementation encounters illegal
characters
**Since:** 10
**See Also:** URLEncoder.encode(java.lang.String, java.nio.charset.Charset)

---

#### Method Detail

decode

```java
@Deprecated

public static
String
decode​(
String
s)
```

Deprecated.

The resulting string may vary depending on the platform's
default encoding. Instead, use the decode(String,String) method
to specify the encoding.

Decodes a

x-www-form-urlencoded

string.
The platform's default encoding is used to determine what characters
are represented by any consecutive sequences of the form
"

%xy

".

**Parameters:** s

- the

String

to decode
**Returns:** the newly decoded

String

---

#### decode

@Deprecated

public static

String

decode​(

String

s)

Decodes a

x-www-form-urlencoded

string.
The platform's default encoding is used to determine what characters
are represented by any consecutive sequences of the form
"

%xy

".

decode

```java
public static
String
decode​(
String
s,

String
enc)
throws
UnsupportedEncodingException
```

Decodes an

application/x-www-form-urlencoded

string using
a specific encoding scheme.

This method behaves the same as

decode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

**Implementation Note:** This implementation will throw an

IllegalArgumentException

when illegal strings are encountered.
**Parameters:** s

- the

String

to decode
**Parameters:** enc

- The name of a supported

character
encoding

.
**Returns:** the newly decoded

String
**Throws:** UnsupportedEncodingException

- If character encoding needs to be consulted, but
named character encoding is not supported
**Since:** 1.4
**See Also:** URLEncoder.encode(java.lang.String, java.lang.String)

---

#### decode

public static

String

decode​(

String

s,

String

enc)
throws

UnsupportedEncodingException

Decodes an

application/x-www-form-urlencoded

string using
a specific encoding scheme.

This method behaves the same as

decode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

This method behaves the same as

decode(java.lang.String,java.nio.charset.Charset)

except that it will

look up the charset

using the given encoding name.

decode

```java
public static
String
decode​(
String
s,

Charset
charset)
```

Decodes an

application/x-www-form-urlencoded

string using
a specific

Charset

.
The supplied charset is used to determine
what characters are represented by any consecutive sequences of the
form "

%xy

".

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce
incompatibilities.

**Implementation Note:** This implementation will throw an

IllegalArgumentException

when illegal strings are encountered.
**Parameters:** s

- the

String

to decode
**Parameters:** charset

- the given charset
**Returns:** the newly decoded

String
**Throws:** NullPointerException

- if

s

or

charset

is

null
**Throws:** IllegalArgumentException

- if the implementation encounters illegal
characters
**Since:** 10
**See Also:** URLEncoder.encode(java.lang.String, java.nio.charset.Charset)

---

#### decode

public static

String

decode​(

String

s,

Charset

charset)

Decodes an

application/x-www-form-urlencoded

string using
a specific

Charset

.
The supplied charset is used to determine
what characters are represented by any consecutive sequences of the
form "

%xy

".

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce
incompatibilities.

Note:

The

World Wide Web Consortium Recommendation

states that
UTF-8 should be used. Not doing so may introduce
incompatibilities.

---

