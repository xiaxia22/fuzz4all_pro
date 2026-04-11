# Class SNIHostName

**Source:** `java.base\javax\net\ssl\SNIHostName.html`

### Class Description

```java
public final class
SNIHostName

extends
SNIServerName
```

Instances of this class represent a server name of type

host_name

in a Server Name
Indication (SNI) extension.

As described in section 3, "Server Name Indication", of

TLS Extensions (RFC 6066)

,
"HostName" contains the fully qualified DNS hostname of the server, as
understood by the client. The encoded server name value of a hostname is
represented as a byte string using ASCII encoding without a trailing dot.
This allows the support of Internationalized Domain Names (IDN) through
the use of A-labels (the ASCII-Compatible Encoding (ACE) form of a valid
string of Internationalized Domain Names for Applications (IDNA)) defined
in

RFC 5890

.

Note that

SNIHostName

objects are immutable.

**Since:** 1.8
**See Also:** SNIServerName

,

StandardConstants.SNI_HOST_NAME

---

### Field Details

*No entries found.*

### Constructor Details

#### public SNIHostName​(
String
hostname)

Creates an

SNIHostName

using the specified hostname.

Note that per

RFC 6066

,
the encoded server name value of a hostname is

StandardCharsets.US_ASCII

-compliant. In this method,

hostname

can be a user-friendly Internationalized Domain Name
(IDN).

IDN.toASCII(String, int)

is used to enforce the
restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

) and
translate the

hostname

into ASCII Compatible Encoding (ACE), as:

```java
IDN.toASCII(hostname, IDN.USE_STD3_ASCII_RULES);
```

The

hostname

argument is illegal if it:

- hostname

is empty,
- hostname

ends with a trailing dot,
- hostname

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

**Parameters:**
- hostname

- the hostname of this server name

**Throws:**
- NullPointerException

- if

hostname

is

null
- IllegalArgumentException

- if

hostname

is illegal

---

#### public SNIHostName​(byte[] encoded)

Creates an

SNIHostName

using the specified encoded value.

This method is normally used to parse the encoded name value in a
requested SNI extension.

Per

RFC 6066

,
the encoded name value of a hostname is

StandardCharsets.US_ASCII

-compliant. However, in the previous
version of the SNI extension (

RFC 4366

),
the encoded hostname is represented as a byte string using UTF-8
encoding. For the purpose of version tolerance, this method allows
that the charset of

encoded

argument can be

StandardCharsets.UTF_8

, as well as

StandardCharsets.US_ASCII

.

IDN.toASCII(String)

is used
to translate the

encoded

argument into ASCII Compatible
Encoding (ACE) hostname.

It is strongly recommended that this constructor is only used to parse
the encoded name value in a requested SNI extension. Otherwise, to
comply with

RFC 6066

,
please always use

StandardCharsets.US_ASCII

-compliant charset
and enforce the restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

)
for

encoded

argument, or use

SNIHostName(String)

instead.

The

encoded

argument is illegal if it:

- encoded

is empty,
- encoded

ends with a trailing dot,
- encoded

is not encoded in

StandardCharsets.US_ASCII

or

StandardCharsets.UTF_8

-compliant charset,
- encoded

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that the

encoded

byte array is cloned
to protect against subsequent modification.

**Parameters:**
- encoded

- the encoded hostname of this server name

**Throws:**
- NullPointerException

- if

encoded

is

null
- IllegalArgumentException

- if

encoded

is illegal

---

### Method Details

#### public
String
getAsciiName()

Returns the

StandardCharsets.US_ASCII

-compliant hostname of
this

SNIHostName

object.

Note that, per

RFC 6066

, the
returned hostname may be an internationalized domain name that
contains A-labels. See

RFC 5890

for more information about the detailed A-label specification.

**Returns:**
- the

StandardCharsets.US_ASCII

-compliant hostname
of this

SNIHostName

object

---

#### public boolean equals​(
Object
other)

Compares this server name to the specified object.

Per

RFC 6066

, DNS
hostnames are case-insensitive. Two server hostnames are equal if,
and only if, they have the same name type, and the hostnames are
equal in a case-independent comparison.

**Overrides:**
- equals

in class

SNIServerName

**Parameters:**
- other

- the other server name object to compare with.

**Returns:**
- true if, and only if, the

other

is considered
equal to this instance

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this

SNIHostName

.

The hash code value is generated using the case-insensitive hostname
of this

SNIHostName

.

**Overrides:**
- hashCode

in class

SNIServerName

**Returns:**
- a hash code value for this

SNIHostName

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of the object, including the DNS
hostname in this

SNIHostName

object.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=host_name (0), value=<hostname>"
```

The "<hostname>" is an ASCII representation of the hostname,
which may contains A-labels. For example, a returned value of an pseudo
hostname may look like:

```java
"type=host_name (0), value=www.example.com"
```

or

```java
"type=host_name (0), value=xn--fsqu00a.xn--0zwm56d"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change.

**Overrides:**
- toString

in class

SNIServerName

**Returns:**
- a string representation of the object.

---

#### public static
SNIMatcher
createSNIMatcher​(
String
regex)

Creates an

SNIMatcher

object for

SNIHostName

s.

This method can be used by a server to verify the acceptable

SNIHostName

s. For example,

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.com");
```

will accept the hostname "www.example.com".

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.(com|org)");
```

will accept hostnames "www.example.com" and "www.example.org".

**Parameters:**
- regex

- the

regular expression pattern

representing the hostname(s) to match

**Returns:**
- a

SNIMatcher

object for

SNIHostName

s

**Throws:**
- NullPointerException

- if

regex

is

null
- PatternSyntaxException

- if the regular expression's
syntax is invalid

---

### Additional Sections

#### Class SNIHostName

java.lang.Object

- javax.net.ssl.SNIServerName
- - javax.net.ssl.SNIHostName

javax.net.ssl.SNIServerName

- javax.net.ssl.SNIHostName

javax.net.ssl.SNIHostName

```java
public final class
SNIHostName

extends
SNIServerName
```

Instances of this class represent a server name of type

host_name

in a Server Name
Indication (SNI) extension.

As described in section 3, "Server Name Indication", of

TLS Extensions (RFC 6066)

,
"HostName" contains the fully qualified DNS hostname of the server, as
understood by the client. The encoded server name value of a hostname is
represented as a byte string using ASCII encoding without a trailing dot.
This allows the support of Internationalized Domain Names (IDN) through
the use of A-labels (the ASCII-Compatible Encoding (ACE) form of a valid
string of Internationalized Domain Names for Applications (IDNA)) defined
in

RFC 5890

.

Note that

SNIHostName

objects are immutable.

**Since:** 1.8
**See Also:** SNIServerName

,

StandardConstants.SNI_HOST_NAME

public final class

SNIHostName

extends

SNIServerName

Instances of this class represent a server name of type

host_name

in a Server Name
Indication (SNI) extension.

As described in section 3, "Server Name Indication", of

TLS Extensions (RFC 6066)

,
"HostName" contains the fully qualified DNS hostname of the server, as
understood by the client. The encoded server name value of a hostname is
represented as a byte string using ASCII encoding without a trailing dot.
This allows the support of Internationalized Domain Names (IDN) through
the use of A-labels (the ASCII-Compatible Encoding (ACE) form of a valid
string of Internationalized Domain Names for Applications (IDNA)) defined
in

RFC 5890

.

Note that

SNIHostName

objects are immutable.

As described in section 3, "Server Name Indication", of

TLS Extensions (RFC 6066)

,
"HostName" contains the fully qualified DNS hostname of the server, as
understood by the client. The encoded server name value of a hostname is
represented as a byte string using ASCII encoding without a trailing dot.
This allows the support of Internationalized Domain Names (IDN) through
the use of A-labels (the ASCII-Compatible Encoding (ACE) form of a valid
string of Internationalized Domain Names for Applications (IDNA)) defined
in

RFC 5890

.

Note that

SNIHostName

objects are immutable.

Note that

SNIHostName

objects are immutable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SNIHostName

​(byte[] encoded)

Creates an

SNIHostName

using the specified encoded value.

SNIHostName

​(

String

hostname)

Creates an

SNIHostName

using the specified hostname.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

SNIMatcher

createSNIMatcher

​(

String

regex)

Creates an

SNIMatcher

object for

SNIHostName

s.

boolean

equals

​(

Object

other)

Compares this server name to the specified object.

String

getAsciiName

()

Returns the

StandardCharsets.US_ASCII

-compliant hostname of
this

SNIHostName

object.

int

hashCode

()

Returns a hash code value for this

SNIHostName

.

String

toString

()

Returns a string representation of the object, including the DNS
hostname in this

SNIHostName

object.

- Methods declared in class javax.net.ssl.

SNIServerName

getEncoded

,

getType

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

Constructor Summary

Constructors

Constructor

Description

SNIHostName

​(byte[] encoded)

Creates an

SNIHostName

using the specified encoded value.

SNIHostName

​(

String

hostname)

Creates an

SNIHostName

using the specified hostname.

---

#### Constructor Summary

Creates an

SNIHostName

using the specified encoded value.

Creates an

SNIHostName

using the specified hostname.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

SNIMatcher

createSNIMatcher

​(

String

regex)

Creates an

SNIMatcher

object for

SNIHostName

s.

boolean

equals

​(

Object

other)

Compares this server name to the specified object.

String

getAsciiName

()

Returns the

StandardCharsets.US_ASCII

-compliant hostname of
this

SNIHostName

object.

int

hashCode

()

Returns a hash code value for this

SNIHostName

.

String

toString

()

Returns a string representation of the object, including the DNS
hostname in this

SNIHostName

object.

- Methods declared in class javax.net.ssl.

SNIServerName

getEncoded

,

getType

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

Creates an

SNIMatcher

object for

SNIHostName

s.

Compares this server name to the specified object.

Returns the

StandardCharsets.US_ASCII

-compliant hostname of
this

SNIHostName

object.

Returns a hash code value for this

SNIHostName

.

Returns a string representation of the object, including the DNS
hostname in this

SNIHostName

object.

Methods declared in class javax.net.ssl.

SNIServerName

getEncoded

,

getType

---

#### Methods declared in class javax.net.ssl. SNIServerName

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SNIHostName

```java
public SNIHostName​(
String
hostname)
```

Creates an

SNIHostName

using the specified hostname.

Note that per

RFC 6066

,
the encoded server name value of a hostname is

StandardCharsets.US_ASCII

-compliant. In this method,

hostname

can be a user-friendly Internationalized Domain Name
(IDN).

IDN.toASCII(String, int)

is used to enforce the
restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

) and
translate the

hostname

into ASCII Compatible Encoding (ACE), as:

```java
IDN.toASCII(hostname, IDN.USE_STD3_ASCII_RULES);
```

The

hostname

argument is illegal if it:

- hostname

is empty,
- hostname

ends with a trailing dot,
- hostname

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

**Parameters:** hostname

- the hostname of this server name
**Throws:** NullPointerException

- if

hostname

is

null
**Throws:** IllegalArgumentException

- if

hostname

is illegal

- SNIHostName

```java
public SNIHostName​(byte[] encoded)
```

Creates an

SNIHostName

using the specified encoded value.

This method is normally used to parse the encoded name value in a
requested SNI extension.

Per

RFC 6066

,
the encoded name value of a hostname is

StandardCharsets.US_ASCII

-compliant. However, in the previous
version of the SNI extension (

RFC 4366

),
the encoded hostname is represented as a byte string using UTF-8
encoding. For the purpose of version tolerance, this method allows
that the charset of

encoded

argument can be

StandardCharsets.UTF_8

, as well as

StandardCharsets.US_ASCII

.

IDN.toASCII(String)

is used
to translate the

encoded

argument into ASCII Compatible
Encoding (ACE) hostname.

It is strongly recommended that this constructor is only used to parse
the encoded name value in a requested SNI extension. Otherwise, to
comply with

RFC 6066

,
please always use

StandardCharsets.US_ASCII

-compliant charset
and enforce the restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

)
for

encoded

argument, or use

SNIHostName(String)

instead.

The

encoded

argument is illegal if it:

- encoded

is empty,
- encoded

ends with a trailing dot,
- encoded

is not encoded in

StandardCharsets.US_ASCII

or

StandardCharsets.UTF_8

-compliant charset,
- encoded

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that the

encoded

byte array is cloned
to protect against subsequent modification.

**Parameters:** encoded

- the encoded hostname of this server name
**Throws:** NullPointerException

- if

encoded

is

null
**Throws:** IllegalArgumentException

- if

encoded

is illegal

============ METHOD DETAIL ==========

- Method Detail

- getAsciiName

```java
public
String
getAsciiName()
```

Returns the

StandardCharsets.US_ASCII

-compliant hostname of
this

SNIHostName

object.

Note that, per

RFC 6066

, the
returned hostname may be an internationalized domain name that
contains A-labels. See

RFC 5890

for more information about the detailed A-label specification.

**Returns:** the

StandardCharsets.US_ASCII

-compliant hostname
of this

SNIHostName

object

- equals

```java
public boolean equals​(
Object
other)
```

Compares this server name to the specified object.

Per

RFC 6066

, DNS
hostnames are case-insensitive. Two server hostnames are equal if,
and only if, they have the same name type, and the hostnames are
equal in a case-independent comparison.

**Overrides:** equals

in class

SNIServerName
**Parameters:** other

- the other server name object to compare with.
**Returns:** true if, and only if, the

other

is considered
equal to this instance
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this

SNIHostName

.

The hash code value is generated using the case-insensitive hostname
of this

SNIHostName

.

**Overrides:** hashCode

in class

SNIServerName
**Returns:** a hash code value for this

SNIHostName

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of the object, including the DNS
hostname in this

SNIHostName

object.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=host_name (0), value=<hostname>"
```

The "<hostname>" is an ASCII representation of the hostname,
which may contains A-labels. For example, a returned value of an pseudo
hostname may look like:

```java
"type=host_name (0), value=www.example.com"
```

or

```java
"type=host_name (0), value=xn--fsqu00a.xn--0zwm56d"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change.

**Overrides:** toString

in class

SNIServerName
**Returns:** a string representation of the object.

- createSNIMatcher

```java
public static
SNIMatcher
createSNIMatcher​(
String
regex)
```

Creates an

SNIMatcher

object for

SNIHostName

s.

This method can be used by a server to verify the acceptable

SNIHostName

s. For example,

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.com");
```

will accept the hostname "www.example.com".

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.(com|org)");
```

will accept hostnames "www.example.com" and "www.example.org".

**Parameters:** regex

- the

regular expression pattern

representing the hostname(s) to match
**Returns:** a

SNIMatcher

object for

SNIHostName

s
**Throws:** NullPointerException

- if

regex

is

null
**Throws:** PatternSyntaxException

- if the regular expression's
syntax is invalid

Constructor Detail

- SNIHostName

```java
public SNIHostName​(
String
hostname)
```

Creates an

SNIHostName

using the specified hostname.

Note that per

RFC 6066

,
the encoded server name value of a hostname is

StandardCharsets.US_ASCII

-compliant. In this method,

hostname

can be a user-friendly Internationalized Domain Name
(IDN).

IDN.toASCII(String, int)

is used to enforce the
restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

) and
translate the

hostname

into ASCII Compatible Encoding (ACE), as:

```java
IDN.toASCII(hostname, IDN.USE_STD3_ASCII_RULES);
```

The

hostname

argument is illegal if it:

- hostname

is empty,
- hostname

ends with a trailing dot,
- hostname

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

**Parameters:** hostname

- the hostname of this server name
**Throws:** NullPointerException

- if

hostname

is

null
**Throws:** IllegalArgumentException

- if

hostname

is illegal

- SNIHostName

```java
public SNIHostName​(byte[] encoded)
```

Creates an

SNIHostName

using the specified encoded value.

This method is normally used to parse the encoded name value in a
requested SNI extension.

Per

RFC 6066

,
the encoded name value of a hostname is

StandardCharsets.US_ASCII

-compliant. However, in the previous
version of the SNI extension (

RFC 4366

),
the encoded hostname is represented as a byte string using UTF-8
encoding. For the purpose of version tolerance, this method allows
that the charset of

encoded

argument can be

StandardCharsets.UTF_8

, as well as

StandardCharsets.US_ASCII

.

IDN.toASCII(String)

is used
to translate the

encoded

argument into ASCII Compatible
Encoding (ACE) hostname.

It is strongly recommended that this constructor is only used to parse
the encoded name value in a requested SNI extension. Otherwise, to
comply with

RFC 6066

,
please always use

StandardCharsets.US_ASCII

-compliant charset
and enforce the restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

)
for

encoded

argument, or use

SNIHostName(String)

instead.

The

encoded

argument is illegal if it:

- encoded

is empty,
- encoded

ends with a trailing dot,
- encoded

is not encoded in

StandardCharsets.US_ASCII

or

StandardCharsets.UTF_8

-compliant charset,
- encoded

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that the

encoded

byte array is cloned
to protect against subsequent modification.

**Parameters:** encoded

- the encoded hostname of this server name
**Throws:** NullPointerException

- if

encoded

is

null
**Throws:** IllegalArgumentException

- if

encoded

is illegal

---

#### Constructor Detail

SNIHostName

```java
public SNIHostName​(
String
hostname)
```

Creates an

SNIHostName

using the specified hostname.

Note that per

RFC 6066

,
the encoded server name value of a hostname is

StandardCharsets.US_ASCII

-compliant. In this method,

hostname

can be a user-friendly Internationalized Domain Name
(IDN).

IDN.toASCII(String, int)

is used to enforce the
restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

) and
translate the

hostname

into ASCII Compatible Encoding (ACE), as:

```java
IDN.toASCII(hostname, IDN.USE_STD3_ASCII_RULES);
```

The

hostname

argument is illegal if it:

- hostname

is empty,
- hostname

ends with a trailing dot,
- hostname

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

**Parameters:** hostname

- the hostname of this server name
**Throws:** NullPointerException

- if

hostname

is

null
**Throws:** IllegalArgumentException

- if

hostname

is illegal

---

#### SNIHostName

public SNIHostName​(

String

hostname)

Creates an

SNIHostName

using the specified hostname.

Note that per

RFC 6066

,
the encoded server name value of a hostname is

StandardCharsets.US_ASCII

-compliant. In this method,

hostname

can be a user-friendly Internationalized Domain Name
(IDN).

IDN.toASCII(String, int)

is used to enforce the
restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

) and
translate the

hostname

into ASCII Compatible Encoding (ACE), as:

```java
IDN.toASCII(hostname, IDN.USE_STD3_ASCII_RULES);
```

The

hostname

argument is illegal if it:

- hostname

is empty,
- hostname

ends with a trailing dot,
- hostname

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that per

RFC 6066

,
the encoded server name value of a hostname is

StandardCharsets.US_ASCII

-compliant. In this method,

hostname

can be a user-friendly Internationalized Domain Name
(IDN).

IDN.toASCII(String, int)

is used to enforce the
restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

) and
translate the

hostname

into ASCII Compatible Encoding (ACE), as:

```java
IDN.toASCII(hostname, IDN.USE_STD3_ASCII_RULES);
```

The

hostname

argument is illegal if it:

- hostname

is empty,
- hostname

ends with a trailing dot,
- hostname

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

IDN.toASCII(hostname, IDN.USE_STD3_ASCII_RULES);

The

hostname

argument is illegal if it:

- hostname

is empty,
- hostname

ends with a trailing dot,
- hostname

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

hostname

is empty,

hostname

ends with a trailing dot,

hostname

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

SNIHostName

```java
public SNIHostName​(byte[] encoded)
```

Creates an

SNIHostName

using the specified encoded value.

This method is normally used to parse the encoded name value in a
requested SNI extension.

Per

RFC 6066

,
the encoded name value of a hostname is

StandardCharsets.US_ASCII

-compliant. However, in the previous
version of the SNI extension (

RFC 4366

),
the encoded hostname is represented as a byte string using UTF-8
encoding. For the purpose of version tolerance, this method allows
that the charset of

encoded

argument can be

StandardCharsets.UTF_8

, as well as

StandardCharsets.US_ASCII

.

IDN.toASCII(String)

is used
to translate the

encoded

argument into ASCII Compatible
Encoding (ACE) hostname.

It is strongly recommended that this constructor is only used to parse
the encoded name value in a requested SNI extension. Otherwise, to
comply with

RFC 6066

,
please always use

StandardCharsets.US_ASCII

-compliant charset
and enforce the restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

)
for

encoded

argument, or use

SNIHostName(String)

instead.

The

encoded

argument is illegal if it:

- encoded

is empty,
- encoded

ends with a trailing dot,
- encoded

is not encoded in

StandardCharsets.US_ASCII

or

StandardCharsets.UTF_8

-compliant charset,
- encoded

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that the

encoded

byte array is cloned
to protect against subsequent modification.

**Parameters:** encoded

- the encoded hostname of this server name
**Throws:** NullPointerException

- if

encoded

is

null
**Throws:** IllegalArgumentException

- if

encoded

is illegal

---

#### SNIHostName

public SNIHostName​(byte[] encoded)

Creates an

SNIHostName

using the specified encoded value.

This method is normally used to parse the encoded name value in a
requested SNI extension.

Per

RFC 6066

,
the encoded name value of a hostname is

StandardCharsets.US_ASCII

-compliant. However, in the previous
version of the SNI extension (

RFC 4366

),
the encoded hostname is represented as a byte string using UTF-8
encoding. For the purpose of version tolerance, this method allows
that the charset of

encoded

argument can be

StandardCharsets.UTF_8

, as well as

StandardCharsets.US_ASCII

.

IDN.toASCII(String)

is used
to translate the

encoded

argument into ASCII Compatible
Encoding (ACE) hostname.

It is strongly recommended that this constructor is only used to parse
the encoded name value in a requested SNI extension. Otherwise, to
comply with

RFC 6066

,
please always use

StandardCharsets.US_ASCII

-compliant charset
and enforce the restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

)
for

encoded

argument, or use

SNIHostName(String)

instead.

The

encoded

argument is illegal if it:

- encoded

is empty,
- encoded

ends with a trailing dot,
- encoded

is not encoded in

StandardCharsets.US_ASCII

or

StandardCharsets.UTF_8

-compliant charset,
- encoded

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that the

encoded

byte array is cloned
to protect against subsequent modification.

This method is normally used to parse the encoded name value in a
requested SNI extension.

Per

RFC 6066

,
the encoded name value of a hostname is

StandardCharsets.US_ASCII

-compliant. However, in the previous
version of the SNI extension (

RFC 4366

),
the encoded hostname is represented as a byte string using UTF-8
encoding. For the purpose of version tolerance, this method allows
that the charset of

encoded

argument can be

StandardCharsets.UTF_8

, as well as

StandardCharsets.US_ASCII

.

IDN.toASCII(String)

is used
to translate the

encoded

argument into ASCII Compatible
Encoding (ACE) hostname.

It is strongly recommended that this constructor is only used to parse
the encoded name value in a requested SNI extension. Otherwise, to
comply with

RFC 6066

,
please always use

StandardCharsets.US_ASCII

-compliant charset
and enforce the restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

)
for

encoded

argument, or use

SNIHostName(String)

instead.

The

encoded

argument is illegal if it:

- encoded

is empty,
- encoded

ends with a trailing dot,
- encoded

is not encoded in

StandardCharsets.US_ASCII

or

StandardCharsets.UTF_8

-compliant charset,
- encoded

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that the

encoded

byte array is cloned
to protect against subsequent modification.

Per

RFC 6066

,
the encoded name value of a hostname is

StandardCharsets.US_ASCII

-compliant. However, in the previous
version of the SNI extension (

RFC 4366

),
the encoded hostname is represented as a byte string using UTF-8
encoding. For the purpose of version tolerance, this method allows
that the charset of

encoded

argument can be

StandardCharsets.UTF_8

, as well as

StandardCharsets.US_ASCII

.

IDN.toASCII(String)

is used
to translate the

encoded

argument into ASCII Compatible
Encoding (ACE) hostname.

It is strongly recommended that this constructor is only used to parse
the encoded name value in a requested SNI extension. Otherwise, to
comply with

RFC 6066

,
please always use

StandardCharsets.US_ASCII

-compliant charset
and enforce the restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

)
for

encoded

argument, or use

SNIHostName(String)

instead.

The

encoded

argument is illegal if it:

- encoded

is empty,
- encoded

ends with a trailing dot,
- encoded

is not encoded in

StandardCharsets.US_ASCII

or

StandardCharsets.UTF_8

-compliant charset,
- encoded

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that the

encoded

byte array is cloned
to protect against subsequent modification.

It is strongly recommended that this constructor is only used to parse
the encoded name value in a requested SNI extension. Otherwise, to
comply with

RFC 6066

,
please always use

StandardCharsets.US_ASCII

-compliant charset
and enforce the restrictions on ASCII characters in hostnames (see

RFC 3490

,

RFC 1122

,

RFC 1123

)
for

encoded

argument, or use

SNIHostName(String)

instead.

The

encoded

argument is illegal if it:

- encoded

is empty,
- encoded

ends with a trailing dot,
- encoded

is not encoded in

StandardCharsets.US_ASCII

or

StandardCharsets.UTF_8

-compliant charset,
- encoded

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that the

encoded

byte array is cloned
to protect against subsequent modification.

The

encoded

argument is illegal if it:

- encoded

is empty,
- encoded

ends with a trailing dot,
- encoded

is not encoded in

StandardCharsets.US_ASCII

or

StandardCharsets.UTF_8

-compliant charset,
- encoded

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that the

encoded

byte array is cloned
to protect against subsequent modification.

encoded

is empty,

encoded

ends with a trailing dot,

encoded

is not encoded in

StandardCharsets.US_ASCII

or

StandardCharsets.UTF_8

-compliant charset,

encoded

is not a valid Internationalized
Domain Name (IDN) compliant with the RFC 3490 specification.

Note that the

encoded

byte array is cloned
to protect against subsequent modification.

Method Detail

- getAsciiName

```java
public
String
getAsciiName()
```

Returns the

StandardCharsets.US_ASCII

-compliant hostname of
this

SNIHostName

object.

Note that, per

RFC 6066

, the
returned hostname may be an internationalized domain name that
contains A-labels. See

RFC 5890

for more information about the detailed A-label specification.

**Returns:** the

StandardCharsets.US_ASCII

-compliant hostname
of this

SNIHostName

object

- equals

```java
public boolean equals​(
Object
other)
```

Compares this server name to the specified object.

Per

RFC 6066

, DNS
hostnames are case-insensitive. Two server hostnames are equal if,
and only if, they have the same name type, and the hostnames are
equal in a case-independent comparison.

**Overrides:** equals

in class

SNIServerName
**Parameters:** other

- the other server name object to compare with.
**Returns:** true if, and only if, the

other

is considered
equal to this instance
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this

SNIHostName

.

The hash code value is generated using the case-insensitive hostname
of this

SNIHostName

.

**Overrides:** hashCode

in class

SNIServerName
**Returns:** a hash code value for this

SNIHostName

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of the object, including the DNS
hostname in this

SNIHostName

object.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=host_name (0), value=<hostname>"
```

The "<hostname>" is an ASCII representation of the hostname,
which may contains A-labels. For example, a returned value of an pseudo
hostname may look like:

```java
"type=host_name (0), value=www.example.com"
```

or

```java
"type=host_name (0), value=xn--fsqu00a.xn--0zwm56d"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change.

**Overrides:** toString

in class

SNIServerName
**Returns:** a string representation of the object.

- createSNIMatcher

```java
public static
SNIMatcher
createSNIMatcher​(
String
regex)
```

Creates an

SNIMatcher

object for

SNIHostName

s.

This method can be used by a server to verify the acceptable

SNIHostName

s. For example,

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.com");
```

will accept the hostname "www.example.com".

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.(com|org)");
```

will accept hostnames "www.example.com" and "www.example.org".

**Parameters:** regex

- the

regular expression pattern

representing the hostname(s) to match
**Returns:** a

SNIMatcher

object for

SNIHostName

s
**Throws:** NullPointerException

- if

regex

is

null
**Throws:** PatternSyntaxException

- if the regular expression's
syntax is invalid

---

#### Method Detail

getAsciiName

```java
public
String
getAsciiName()
```

Returns the

StandardCharsets.US_ASCII

-compliant hostname of
this

SNIHostName

object.

Note that, per

RFC 6066

, the
returned hostname may be an internationalized domain name that
contains A-labels. See

RFC 5890

for more information about the detailed A-label specification.

**Returns:** the

StandardCharsets.US_ASCII

-compliant hostname
of this

SNIHostName

object

---

#### getAsciiName

public

String

getAsciiName()

Returns the

StandardCharsets.US_ASCII

-compliant hostname of
this

SNIHostName

object.

Note that, per

RFC 6066

, the
returned hostname may be an internationalized domain name that
contains A-labels. See

RFC 5890

for more information about the detailed A-label specification.

Note that, per

RFC 6066

, the
returned hostname may be an internationalized domain name that
contains A-labels. See

RFC 5890

for more information about the detailed A-label specification.

equals

```java
public boolean equals​(
Object
other)
```

Compares this server name to the specified object.

Per

RFC 6066

, DNS
hostnames are case-insensitive. Two server hostnames are equal if,
and only if, they have the same name type, and the hostnames are
equal in a case-independent comparison.

**Overrides:** equals

in class

SNIServerName
**Parameters:** other

- the other server name object to compare with.
**Returns:** true if, and only if, the

other

is considered
equal to this instance
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Compares this server name to the specified object.

Per

RFC 6066

, DNS
hostnames are case-insensitive. Two server hostnames are equal if,
and only if, they have the same name type, and the hostnames are
equal in a case-independent comparison.

Per

RFC 6066

, DNS
hostnames are case-insensitive. Two server hostnames are equal if,
and only if, they have the same name type, and the hostnames are
equal in a case-independent comparison.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this

SNIHostName

.

The hash code value is generated using the case-insensitive hostname
of this

SNIHostName

.

**Overrides:** hashCode

in class

SNIServerName
**Returns:** a hash code value for this

SNIHostName

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this

SNIHostName

.

The hash code value is generated using the case-insensitive hostname
of this

SNIHostName

.

The hash code value is generated using the case-insensitive hostname
of this

SNIHostName

.

toString

```java
public
String
toString()
```

Returns a string representation of the object, including the DNS
hostname in this

SNIHostName

object.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=host_name (0), value=<hostname>"
```

The "<hostname>" is an ASCII representation of the hostname,
which may contains A-labels. For example, a returned value of an pseudo
hostname may look like:

```java
"type=host_name (0), value=www.example.com"
```

or

```java
"type=host_name (0), value=xn--fsqu00a.xn--0zwm56d"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change.

**Overrides:** toString

in class

SNIServerName
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string representation of the object, including the DNS
hostname in this

SNIHostName

object.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=host_name (0), value=<hostname>"
```

The "<hostname>" is an ASCII representation of the hostname,
which may contains A-labels. For example, a returned value of an pseudo
hostname may look like:

```java
"type=host_name (0), value=www.example.com"
```

or

```java
"type=host_name (0), value=xn--fsqu00a.xn--0zwm56d"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change.

The exact details of the representation are unspecified and subject
to change, but the following may be regarded as typical:

```java
"type=host_name (0), value=<hostname>"
```

The "<hostname>" is an ASCII representation of the hostname,
which may contains A-labels. For example, a returned value of an pseudo
hostname may look like:

```java
"type=host_name (0), value=www.example.com"
```

or

```java
"type=host_name (0), value=xn--fsqu00a.xn--0zwm56d"
```

Please NOTE that the exact details of the representation are unspecified
and subject to change.

"type=host_name (0), value=<hostname>"

"type=host_name (0), value=www.example.com"

"type=host_name (0), value=xn--fsqu00a.xn--0zwm56d"

Please NOTE that the exact details of the representation are unspecified
and subject to change.

createSNIMatcher

```java
public static
SNIMatcher
createSNIMatcher​(
String
regex)
```

Creates an

SNIMatcher

object for

SNIHostName

s.

This method can be used by a server to verify the acceptable

SNIHostName

s. For example,

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.com");
```

will accept the hostname "www.example.com".

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.(com|org)");
```

will accept hostnames "www.example.com" and "www.example.org".

**Parameters:** regex

- the

regular expression pattern

representing the hostname(s) to match
**Returns:** a

SNIMatcher

object for

SNIHostName

s
**Throws:** NullPointerException

- if

regex

is

null
**Throws:** PatternSyntaxException

- if the regular expression's
syntax is invalid

---

#### createSNIMatcher

public static

SNIMatcher

createSNIMatcher​(

String

regex)

Creates an

SNIMatcher

object for

SNIHostName

s.

This method can be used by a server to verify the acceptable

SNIHostName

s. For example,

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.com");
```

will accept the hostname "www.example.com".

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.(com|org)");
```

will accept hostnames "www.example.com" and "www.example.org".

This method can be used by a server to verify the acceptable

SNIHostName

s. For example,

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.com");
```

will accept the hostname "www.example.com".

```java
SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.(com|org)");
```

will accept hostnames "www.example.com" and "www.example.org".

SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.com");

SNIMatcher matcher =
SNIHostName.createSNIMatcher("www\\.example\\.(com|org)");

---

