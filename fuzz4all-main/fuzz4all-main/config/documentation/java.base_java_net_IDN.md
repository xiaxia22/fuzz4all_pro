# Class IDN

**Source:** `java.base\java\net\IDN.html`

### Class Description

```java
public final class
IDN

extends
Object
```

Provides methods to convert internationalized domain names (IDNs) between
a normal Unicode representation and an ASCII Compatible Encoding (ACE) representation.
Internationalized domain names can use characters from the entire range of
Unicode, while traditional domain names are restricted to ASCII characters.
ACE is an encoding of Unicode strings that uses only ASCII characters and
can be used with software (such as the Domain Name System) that only
understands traditional domain names.

Internationalized domain names are defined in

RFC 3490

.
RFC 3490 defines two operations: ToASCII and ToUnicode. These 2 operations employ

Nameprep

algorithm, which is a
profile of

Stringprep

, and

Punycode

algorithm to convert
domain name string back and forth.

The behavior of aforementioned conversion process can be adjusted by various flags:

- If the ALLOW_UNASSIGNED flag is used, the domain name string to be converted
can contain code points that are unassigned in Unicode 3.2, which is the
Unicode version on which IDN conversion is based. If the flag is not used,
the presence of such unassigned code points is treated as an error.

If the USE_STD3_ASCII_RULES flag is used, ASCII strings are checked against

RFC 1122

and

RFC 1123

.
It is an error if they don't meet the requirements.

These flags can be logically OR'ed together.

The security consideration is important with respect to internationalization
domain name support. For example, English domain names may be

homographed

- maliciously misspelled by substitution of non-Latin letters.

Unicode Technical Report #36

discusses security issues of IDN support as well as possible solutions.
Applications are responsible for taking adequate security measures when using
international domain names.

**Since:** 1.6

---

### Field Details

#### public static final int ALLOW_UNASSIGNED

Flag to allow processing of unassigned code points

**See Also:**
- Constant Field Values

---

#### public static final int USE_STD3_ASCII_RULES

Flag to turn on the check against STD-3 ASCII rules

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
String
toASCII​(
String
input,
int flag)

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

ToASCII operation can fail. ToASCII fails if any step of it fails.
If ToASCII operation fails, an IllegalArgumentException will be thrown.
In this case, the input string should not be used in an internationalized domain name.

A label is an individual part of a domain name. The original ToASCII operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop). if dots are
used as label separators, this method also changes all of them to \u002E (full stop)
in output translated string.

**Parameters:**
- input

- the string to be processed
- flag

- process flag; can be 0 or any logical OR of possible flags

**Returns:**
- the translated

String

**Throws:**
- IllegalArgumentException

- if the input string doesn't conform to RFC 3490 specification

---

#### public static
String
toASCII​(
String
input)

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

This convenience method works as if by invoking the
two-argument counterpart as follows:

toASCII

(input, 0);

**Parameters:**
- input

- the string to be processed

**Returns:**
- the translated

String

**Throws:**
- IllegalArgumentException

- if the input string doesn't conform to RFC 3490 specification

---

#### public static
String
toUnicode​(
String
input,
int flag)

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

ToUnicode never fails. In case of any error, the input string is returned unmodified.

A label is an individual part of a domain name. The original ToUnicode operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop).

**Parameters:**
- input

- the string to be processed
- flag

- process flag; can be 0 or any logical OR of possible flags

**Returns:**
- the translated

String

---

#### public static
String
toUnicode​(
String
input)

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

This convenience method works as if by invoking the
two-argument counterpart as follows:

toUnicode

(input, 0);

**Parameters:**
- input

- the string to be processed

**Returns:**
- the translated

String

---

### Additional Sections

#### Class IDN

java.lang.Object

- java.net.IDN

java.net.IDN

```java
public final class
IDN

extends
Object
```

Provides methods to convert internationalized domain names (IDNs) between
a normal Unicode representation and an ASCII Compatible Encoding (ACE) representation.
Internationalized domain names can use characters from the entire range of
Unicode, while traditional domain names are restricted to ASCII characters.
ACE is an encoding of Unicode strings that uses only ASCII characters and
can be used with software (such as the Domain Name System) that only
understands traditional domain names.

Internationalized domain names are defined in

RFC 3490

.
RFC 3490 defines two operations: ToASCII and ToUnicode. These 2 operations employ

Nameprep

algorithm, which is a
profile of

Stringprep

, and

Punycode

algorithm to convert
domain name string back and forth.

The behavior of aforementioned conversion process can be adjusted by various flags:

- If the ALLOW_UNASSIGNED flag is used, the domain name string to be converted
can contain code points that are unassigned in Unicode 3.2, which is the
Unicode version on which IDN conversion is based. If the flag is not used,
the presence of such unassigned code points is treated as an error.

If the USE_STD3_ASCII_RULES flag is used, ASCII strings are checked against

RFC 1122

and

RFC 1123

.
It is an error if they don't meet the requirements.

These flags can be logically OR'ed together.

The security consideration is important with respect to internationalization
domain name support. For example, English domain names may be

homographed

- maliciously misspelled by substitution of non-Latin letters.

Unicode Technical Report #36

discusses security issues of IDN support as well as possible solutions.
Applications are responsible for taking adequate security measures when using
international domain names.

**Since:** 1.6

public final class

IDN

extends

Object

Provides methods to convert internationalized domain names (IDNs) between
a normal Unicode representation and an ASCII Compatible Encoding (ACE) representation.
Internationalized domain names can use characters from the entire range of
Unicode, while traditional domain names are restricted to ASCII characters.
ACE is an encoding of Unicode strings that uses only ASCII characters and
can be used with software (such as the Domain Name System) that only
understands traditional domain names.

Internationalized domain names are defined in

RFC 3490

.
RFC 3490 defines two operations: ToASCII and ToUnicode. These 2 operations employ

Nameprep

algorithm, which is a
profile of

Stringprep

, and

Punycode

algorithm to convert
domain name string back and forth.

The behavior of aforementioned conversion process can be adjusted by various flags:

- If the ALLOW_UNASSIGNED flag is used, the domain name string to be converted
can contain code points that are unassigned in Unicode 3.2, which is the
Unicode version on which IDN conversion is based. If the flag is not used,
the presence of such unassigned code points is treated as an error.

If the USE_STD3_ASCII_RULES flag is used, ASCII strings are checked against

RFC 1122

and

RFC 1123

.
It is an error if they don't meet the requirements.

These flags can be logically OR'ed together.

The security consideration is important with respect to internationalization
domain name support. For example, English domain names may be

homographed

- maliciously misspelled by substitution of non-Latin letters.

Unicode Technical Report #36

discusses security issues of IDN support as well as possible solutions.
Applications are responsible for taking adequate security measures when using
international domain names.

Internationalized domain names are defined in

RFC 3490

.
RFC 3490 defines two operations: ToASCII and ToUnicode. These 2 operations employ

Nameprep

algorithm, which is a
profile of

Stringprep

, and

Punycode

algorithm to convert
domain name string back and forth.

The behavior of aforementioned conversion process can be adjusted by various flags:

- If the ALLOW_UNASSIGNED flag is used, the domain name string to be converted
can contain code points that are unassigned in Unicode 3.2, which is the
Unicode version on which IDN conversion is based. If the flag is not used,
the presence of such unassigned code points is treated as an error.

If the USE_STD3_ASCII_RULES flag is used, ASCII strings are checked against

RFC 1122

and

RFC 1123

.
It is an error if they don't meet the requirements.

These flags can be logically OR'ed together.

The security consideration is important with respect to internationalization
domain name support. For example, English domain names may be

homographed

- maliciously misspelled by substitution of non-Latin letters.

Unicode Technical Report #36

discusses security issues of IDN support as well as possible solutions.
Applications are responsible for taking adequate security measures when using
international domain names.

The behavior of aforementioned conversion process can be adjusted by various flags:

- If the ALLOW_UNASSIGNED flag is used, the domain name string to be converted
can contain code points that are unassigned in Unicode 3.2, which is the
Unicode version on which IDN conversion is based. If the flag is not used,
the presence of such unassigned code points is treated as an error.

If the USE_STD3_ASCII_RULES flag is used, ASCII strings are checked against

RFC 1122

and

RFC 1123

.
It is an error if they don't meet the requirements.

These flags can be logically OR'ed together.

The security consideration is important with respect to internationalization
domain name support. For example, English domain names may be

homographed

- maliciously misspelled by substitution of non-Latin letters.

Unicode Technical Report #36

discusses security issues of IDN support as well as possible solutions.
Applications are responsible for taking adequate security measures when using
international domain names.

If the ALLOW_UNASSIGNED flag is used, the domain name string to be converted
can contain code points that are unassigned in Unicode 3.2, which is the
Unicode version on which IDN conversion is based. If the flag is not used,
the presence of such unassigned code points is treated as an error.

If the USE_STD3_ASCII_RULES flag is used, ASCII strings are checked against

RFC 1122

and

RFC 1123

.
It is an error if they don't meet the requirements.

The security consideration is important with respect to internationalization
domain name support. For example, English domain names may be

homographed

- maliciously misspelled by substitution of non-Latin letters.

Unicode Technical Report #36

discusses security issues of IDN support as well as possible solutions.
Applications are responsible for taking adequate security measures when using
international domain names.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ALLOW_UNASSIGNED

Flag to allow processing of unassigned code points

static int

USE_STD3_ASCII_RULES

Flag to turn on the check against STD-3 ASCII rules

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

String

toASCII

​(

String

input)

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

static

String

toASCII

​(

String

input,
int flag)

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

static

String

toUnicode

​(

String

input)

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

static

String

toUnicode

​(

String

input,
int flag)

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

ALLOW_UNASSIGNED

Flag to allow processing of unassigned code points

static int

USE_STD3_ASCII_RULES

Flag to turn on the check against STD-3 ASCII rules

---

#### Field Summary

Flag to allow processing of unassigned code points

Flag to turn on the check against STD-3 ASCII rules

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

String

toASCII

​(

String

input)

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

static

String

toASCII

​(

String

input,
int flag)

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

static

String

toUnicode

​(

String

input)

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

static

String

toUnicode

​(

String

input,
int flag)

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

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

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

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

============ FIELD DETAIL ===========

- Field Detail

- ALLOW_UNASSIGNED

```java
public static final int ALLOW_UNASSIGNED
```

Flag to allow processing of unassigned code points

**See Also:** Constant Field Values

- USE_STD3_ASCII_RULES

```java
public static final int USE_STD3_ASCII_RULES
```

Flag to turn on the check against STD-3 ASCII rules

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- toASCII

```java
public static
String
toASCII​(
String
input,
int flag)
```

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

ToASCII operation can fail. ToASCII fails if any step of it fails.
If ToASCII operation fails, an IllegalArgumentException will be thrown.
In this case, the input string should not be used in an internationalized domain name.

A label is an individual part of a domain name. The original ToASCII operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop). if dots are
used as label separators, this method also changes all of them to \u002E (full stop)
in output translated string.

**Parameters:** input

- the string to be processed
**Parameters:** flag

- process flag; can be 0 or any logical OR of possible flags
**Returns:** the translated

String
**Throws:** IllegalArgumentException

- if the input string doesn't conform to RFC 3490 specification

- toASCII

```java
public static
String
toASCII​(
String
input)
```

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

This convenience method works as if by invoking the
two-argument counterpart as follows:

toASCII

(input, 0);

**Parameters:** input

- the string to be processed
**Returns:** the translated

String
**Throws:** IllegalArgumentException

- if the input string doesn't conform to RFC 3490 specification

- toUnicode

```java
public static
String
toUnicode​(
String
input,
int flag)
```

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

ToUnicode never fails. In case of any error, the input string is returned unmodified.

A label is an individual part of a domain name. The original ToUnicode operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop).

**Parameters:** input

- the string to be processed
**Parameters:** flag

- process flag; can be 0 or any logical OR of possible flags
**Returns:** the translated

String

- toUnicode

```java
public static
String
toUnicode​(
String
input)
```

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

This convenience method works as if by invoking the
two-argument counterpart as follows:

toUnicode

(input, 0);

**Parameters:** input

- the string to be processed
**Returns:** the translated

String

Field Detail

- ALLOW_UNASSIGNED

```java
public static final int ALLOW_UNASSIGNED
```

Flag to allow processing of unassigned code points

**See Also:** Constant Field Values

- USE_STD3_ASCII_RULES

```java
public static final int USE_STD3_ASCII_RULES
```

Flag to turn on the check against STD-3 ASCII rules

**See Also:** Constant Field Values

---

#### Field Detail

ALLOW_UNASSIGNED

```java
public static final int ALLOW_UNASSIGNED
```

Flag to allow processing of unassigned code points

**See Also:** Constant Field Values

---

#### ALLOW_UNASSIGNED

public static final int ALLOW_UNASSIGNED

Flag to allow processing of unassigned code points

USE_STD3_ASCII_RULES

```java
public static final int USE_STD3_ASCII_RULES
```

Flag to turn on the check against STD-3 ASCII rules

**See Also:** Constant Field Values

---

#### USE_STD3_ASCII_RULES

public static final int USE_STD3_ASCII_RULES

Flag to turn on the check against STD-3 ASCII rules

Method Detail

- toASCII

```java
public static
String
toASCII​(
String
input,
int flag)
```

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

ToASCII operation can fail. ToASCII fails if any step of it fails.
If ToASCII operation fails, an IllegalArgumentException will be thrown.
In this case, the input string should not be used in an internationalized domain name.

A label is an individual part of a domain name. The original ToASCII operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop). if dots are
used as label separators, this method also changes all of them to \u002E (full stop)
in output translated string.

**Parameters:** input

- the string to be processed
**Parameters:** flag

- process flag; can be 0 or any logical OR of possible flags
**Returns:** the translated

String
**Throws:** IllegalArgumentException

- if the input string doesn't conform to RFC 3490 specification

- toASCII

```java
public static
String
toASCII​(
String
input)
```

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

This convenience method works as if by invoking the
two-argument counterpart as follows:

toASCII

(input, 0);

**Parameters:** input

- the string to be processed
**Returns:** the translated

String
**Throws:** IllegalArgumentException

- if the input string doesn't conform to RFC 3490 specification

- toUnicode

```java
public static
String
toUnicode​(
String
input,
int flag)
```

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

ToUnicode never fails. In case of any error, the input string is returned unmodified.

A label is an individual part of a domain name. The original ToUnicode operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop).

**Parameters:** input

- the string to be processed
**Parameters:** flag

- process flag; can be 0 or any logical OR of possible flags
**Returns:** the translated

String

- toUnicode

```java
public static
String
toUnicode​(
String
input)
```

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

This convenience method works as if by invoking the
two-argument counterpart as follows:

toUnicode

(input, 0);

**Parameters:** input

- the string to be processed
**Returns:** the translated

String

---

#### Method Detail

toASCII

```java
public static
String
toASCII​(
String
input,
int flag)
```

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

ToASCII operation can fail. ToASCII fails if any step of it fails.
If ToASCII operation fails, an IllegalArgumentException will be thrown.
In this case, the input string should not be used in an internationalized domain name.

A label is an individual part of a domain name. The original ToASCII operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop). if dots are
used as label separators, this method also changes all of them to \u002E (full stop)
in output translated string.

**Parameters:** input

- the string to be processed
**Parameters:** flag

- process flag; can be 0 or any logical OR of possible flags
**Returns:** the translated

String
**Throws:** IllegalArgumentException

- if the input string doesn't conform to RFC 3490 specification

---

#### toASCII

public static

String

toASCII​(

String

input,
int flag)

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

ToASCII operation can fail. ToASCII fails if any step of it fails.
If ToASCII operation fails, an IllegalArgumentException will be thrown.
In this case, the input string should not be used in an internationalized domain name.

A label is an individual part of a domain name. The original ToASCII operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop). if dots are
used as label separators, this method also changes all of them to \u002E (full stop)
in output translated string.

ToASCII operation can fail. ToASCII fails if any step of it fails.
If ToASCII operation fails, an IllegalArgumentException will be thrown.
In this case, the input string should not be used in an internationalized domain name.

A label is an individual part of a domain name. The original ToASCII operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop). if dots are
used as label separators, this method also changes all of them to \u002E (full stop)
in output translated string.

A label is an individual part of a domain name. The original ToASCII operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop). if dots are
used as label separators, this method also changes all of them to \u002E (full stop)
in output translated string.

toASCII

```java
public static
String
toASCII​(
String
input)
```

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

This convenience method works as if by invoking the
two-argument counterpart as follows:

toASCII

(input, 0);

**Parameters:** input

- the string to be processed
**Returns:** the translated

String
**Throws:** IllegalArgumentException

- if the input string doesn't conform to RFC 3490 specification

---

#### toASCII

public static

String

toASCII​(

String

input)

Translates a string from Unicode to ASCII Compatible Encoding (ACE),
as defined by the ToASCII operation of

RFC 3490

.

This convenience method works as if by invoking the
two-argument counterpart as follows:

toASCII

(input, 0);

This convenience method works as if by invoking the
two-argument counterpart as follows:

toASCII

(input, 0);

toUnicode

```java
public static
String
toUnicode​(
String
input,
int flag)
```

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

ToUnicode never fails. In case of any error, the input string is returned unmodified.

A label is an individual part of a domain name. The original ToUnicode operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop).

**Parameters:** input

- the string to be processed
**Parameters:** flag

- process flag; can be 0 or any logical OR of possible flags
**Returns:** the translated

String

---

#### toUnicode

public static

String

toUnicode​(

String

input,
int flag)

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

ToUnicode never fails. In case of any error, the input string is returned unmodified.

A label is an individual part of a domain name. The original ToUnicode operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop).

ToUnicode never fails. In case of any error, the input string is returned unmodified.

A label is an individual part of a domain name. The original ToUnicode operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop).

A label is an individual part of a domain name. The original ToUnicode operation,
as defined in RFC 3490, only operates on a single label. This method can handle
both label and entire domain name, by assuming that labels in a domain name are
always separated by dots. The following characters are recognized as dots:
\u002E (full stop), \u3002 (ideographic full stop), \uFF0E (fullwidth full stop),
and \uFF61 (halfwidth ideographic full stop).

toUnicode

```java
public static
String
toUnicode​(
String
input)
```

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

This convenience method works as if by invoking the
two-argument counterpart as follows:

toUnicode

(input, 0);

**Parameters:** input

- the string to be processed
**Returns:** the translated

String

---

#### toUnicode

public static

String

toUnicode​(

String

input)

Translates a string from ASCII Compatible Encoding (ACE) to Unicode,
as defined by the ToUnicode operation of

RFC 3490

.

This convenience method works as if by invoking the
two-argument counterpart as follows:

toUnicode

(input, 0);

This convenience method works as if by invoking the
two-argument counterpart as follows:

toUnicode

(input, 0);

---

