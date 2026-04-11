# Class ReferenceUriSchemesSupported

**Source:** `java.desktop\javax\print\attribute\standard\ReferenceUriSchemesSupported.html`

### Class Description

```java
public class
ReferenceUriSchemesSupported

extends
EnumSyntax

implements
Attribute
```

Class

ReferenceUriSchemesSupported

is a printing attribute class an
enumeration, that indicates a "URI scheme," such as "http:" or "ftp:", that a
printer can use to retrieve print data stored at a

URI

location. If a
printer supports doc flavors with a print data representation class of

"java.net.URL"

, the printer uses instances of class

ReferenceUriSchemesSupported

to advertise the

URI

schemes it
can accept. The acceptable

URI

schemes are included as service
attributes in the lookup service; this lets clients search the for printers
that can get print data using a certain

URI

scheme. The acceptable

URI

schemes can also be queried using the capability methods in
interface

PrintService

. However,

ReferenceUriSchemesSupported

attributes are used solely for determining acceptable

URI

schemes,
they are never included in a doc's, print request's, print job's, or print
service's attribute set.

The Internet Assigned Numbers Authority maintains the

official list of
URI schemes

.

Class

ReferenceUriSchemesSupported

defines enumeration values for
widely used

URI

schemes. A printer that supports additional

URI

schemes can define them in a subclass of class

ReferenceUriSchemesSupported

.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

---

### Field Details

#### public static final
ReferenceUriSchemesSupported
FTP

File Transfer Protocol (FTP).

---

#### public static final
ReferenceUriSchemesSupported
HTTP

HyperText Transfer Protocol (HTTP).

---

#### public static final
ReferenceUriSchemesSupported
HTTPS

Secure HyperText Transfer Protocol (HTTPS).

---

#### public static final
ReferenceUriSchemesSupported
GOPHER

Gopher Protocol.

---

#### public static final
ReferenceUriSchemesSupported
NEWS

USENET news.

---

#### public static final
ReferenceUriSchemesSupported
NNTP

USENET news using Network News Transfer Protocol (NNTP).

---

#### public static final
ReferenceUriSchemesSupported
WAIS

Wide Area Information Server (WAIS) protocol.

---

#### public static final
ReferenceUriSchemesSupported
FILE

Host-specific file names.

---

### Constructor Details

#### protected ReferenceUriSchemesSupported​(int value)

Construct a new reference

URI

scheme enumeration value with the
given integer value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

ReferenceUriSchemesSupported

.

**Overrides:**
- getStringTable

in class

EnumSyntax

**Returns:**
- the string table

---

#### protected
EnumSyntax
[] getEnumValueTable()

Returns the enumeration value table for class

ReferenceUriSchemesSupported

.

**Overrides:**
- getEnumValueTable

in class

EnumSyntax

**Returns:**
- the value table

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category is class

ReferenceUriSchemesSupported

itself.

**Specified by:**
- getCategory

in interface

Attribute

**Returns:**
- printing attribute class (category), an instance of class

java.lang.Class

---

#### public final
String
getName()

Get the name of the category of which this attribute value is an
instance.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category name is

"reference-uri-schemes-supported"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class ReferenceUriSchemesSupported

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.ReferenceUriSchemesSupported

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.ReferenceUriSchemesSupported

javax.print.attribute.standard.ReferenceUriSchemesSupported

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

```java
public class
ReferenceUriSchemesSupported

extends
EnumSyntax

implements
Attribute
```

Class

ReferenceUriSchemesSupported

is a printing attribute class an
enumeration, that indicates a "URI scheme," such as "http:" or "ftp:", that a
printer can use to retrieve print data stored at a

URI

location. If a
printer supports doc flavors with a print data representation class of

"java.net.URL"

, the printer uses instances of class

ReferenceUriSchemesSupported

to advertise the

URI

schemes it
can accept. The acceptable

URI

schemes are included as service
attributes in the lookup service; this lets clients search the for printers
that can get print data using a certain

URI

scheme. The acceptable

URI

schemes can also be queried using the capability methods in
interface

PrintService

. However,

ReferenceUriSchemesSupported

attributes are used solely for determining acceptable

URI

schemes,
they are never included in a doc's, print request's, print job's, or print
service's attribute set.

The Internet Assigned Numbers Authority maintains the

official list of
URI schemes

.

Class

ReferenceUriSchemesSupported

defines enumeration values for
widely used

URI

schemes. A printer that supports additional

URI

schemes can define them in a subclass of class

ReferenceUriSchemesSupported

.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**See Also:** Serialized Form

public class

ReferenceUriSchemesSupported

extends

EnumSyntax

implements

Attribute

Class

ReferenceUriSchemesSupported

is a printing attribute class an
enumeration, that indicates a "URI scheme," such as "http:" or "ftp:", that a
printer can use to retrieve print data stored at a

URI

location. If a
printer supports doc flavors with a print data representation class of

"java.net.URL"

, the printer uses instances of class

ReferenceUriSchemesSupported

to advertise the

URI

schemes it
can accept. The acceptable

URI

schemes are included as service
attributes in the lookup service; this lets clients search the for printers
that can get print data using a certain

URI

scheme. The acceptable

URI

schemes can also be queried using the capability methods in
interface

PrintService

. However,

ReferenceUriSchemesSupported

attributes are used solely for determining acceptable

URI

schemes,
they are never included in a doc's, print request's, print job's, or print
service's attribute set.

The Internet Assigned Numbers Authority maintains the

official list of
URI schemes

.

Class

ReferenceUriSchemesSupported

defines enumeration values for
widely used

URI

schemes. A printer that supports additional

URI

schemes can define them in a subclass of class

ReferenceUriSchemesSupported

.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

The Internet Assigned Numbers Authority maintains the

official list of
URI schemes

.

Class

ReferenceUriSchemesSupported

defines enumeration values for
widely used

URI

schemes. A printer that supports additional

URI

schemes can define them in a subclass of class

ReferenceUriSchemesSupported

.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

Class

ReferenceUriSchemesSupported

defines enumeration values for
widely used

URI

schemes. A printer that supports additional

URI

schemes can define them in a subclass of class

ReferenceUriSchemesSupported

.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ReferenceUriSchemesSupported

FILE

Host-specific file names.

static

ReferenceUriSchemesSupported

FTP

File Transfer Protocol (FTP).

static

ReferenceUriSchemesSupported

GOPHER

Gopher Protocol.

static

ReferenceUriSchemesSupported

HTTP

HyperText Transfer Protocol (HTTP).

static

ReferenceUriSchemesSupported

HTTPS

Secure HyperText Transfer Protocol (HTTPS).

static

ReferenceUriSchemesSupported

NEWS

USENET news.

static

ReferenceUriSchemesSupported

NNTP

USENET news using Network News Transfer Protocol (NNTP).

static

ReferenceUriSchemesSupported

WAIS

Wide Area Information Server (WAIS) protocol.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ReferenceUriSchemesSupported

​(int value)

Construct a new reference

URI

scheme enumeration value with the
given integer value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

ReferenceUriSchemesSupported

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

ReferenceUriSchemesSupported

.

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

equals

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

Field Summary

Fields

Modifier and Type

Field

Description

static

ReferenceUriSchemesSupported

FILE

Host-specific file names.

static

ReferenceUriSchemesSupported

FTP

File Transfer Protocol (FTP).

static

ReferenceUriSchemesSupported

GOPHER

Gopher Protocol.

static

ReferenceUriSchemesSupported

HTTP

HyperText Transfer Protocol (HTTP).

static

ReferenceUriSchemesSupported

HTTPS

Secure HyperText Transfer Protocol (HTTPS).

static

ReferenceUriSchemesSupported

NEWS

USENET news.

static

ReferenceUriSchemesSupported

NNTP

USENET news using Network News Transfer Protocol (NNTP).

static

ReferenceUriSchemesSupported

WAIS

Wide Area Information Server (WAIS) protocol.

---

#### Field Summary

Host-specific file names.

File Transfer Protocol (FTP).

Gopher Protocol.

HyperText Transfer Protocol (HTTP).

Secure HyperText Transfer Protocol (HTTPS).

USENET news.

USENET news using Network News Transfer Protocol (NNTP).

Wide Area Information Server (WAIS) protocol.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ReferenceUriSchemesSupported

​(int value)

Construct a new reference

URI

scheme enumeration value with the
given integer value.

---

#### Constructor Summary

Construct a new reference

URI

scheme enumeration value with the
given integer value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

ReferenceUriSchemesSupported

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

ReferenceUriSchemesSupported

.

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

equals

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

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Returns the enumeration value table for class

ReferenceUriSchemesSupported

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

ReferenceUriSchemesSupported

.

Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

---

#### Methods declared in class javax.print.attribute. EnumSyntax

Methods declared in class java.lang.

Object

equals

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

============ FIELD DETAIL ===========

- Field Detail

- FTP

```java
public static final
ReferenceUriSchemesSupported
FTP
```

File Transfer Protocol (FTP).

- HTTP

```java
public static final
ReferenceUriSchemesSupported
HTTP
```

HyperText Transfer Protocol (HTTP).

- HTTPS

```java
public static final
ReferenceUriSchemesSupported
HTTPS
```

Secure HyperText Transfer Protocol (HTTPS).

- GOPHER

```java
public static final
ReferenceUriSchemesSupported
GOPHER
```

Gopher Protocol.

- NEWS

```java
public static final
ReferenceUriSchemesSupported
NEWS
```

USENET news.

- NNTP

```java
public static final
ReferenceUriSchemesSupported
NNTP
```

USENET news using Network News Transfer Protocol (NNTP).

- WAIS

```java
public static final
ReferenceUriSchemesSupported
WAIS
```

Wide Area Information Server (WAIS) protocol.

- FILE

```java
public static final
ReferenceUriSchemesSupported
FILE
```

Host-specific file names.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ReferenceUriSchemesSupported

```java
protected ReferenceUriSchemesSupported​(int value)
```

Construct a new reference

URI

scheme enumeration value with the
given integer value.

**Parameters:** value

- Integer value

============ METHOD DETAIL ==========

- Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

ReferenceUriSchemesSupported

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

ReferenceUriSchemesSupported

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category is class

ReferenceUriSchemesSupported

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category name is

"reference-uri-schemes-supported"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- FTP

```java
public static final
ReferenceUriSchemesSupported
FTP
```

File Transfer Protocol (FTP).

- HTTP

```java
public static final
ReferenceUriSchemesSupported
HTTP
```

HyperText Transfer Protocol (HTTP).

- HTTPS

```java
public static final
ReferenceUriSchemesSupported
HTTPS
```

Secure HyperText Transfer Protocol (HTTPS).

- GOPHER

```java
public static final
ReferenceUriSchemesSupported
GOPHER
```

Gopher Protocol.

- NEWS

```java
public static final
ReferenceUriSchemesSupported
NEWS
```

USENET news.

- NNTP

```java
public static final
ReferenceUriSchemesSupported
NNTP
```

USENET news using Network News Transfer Protocol (NNTP).

- WAIS

```java
public static final
ReferenceUriSchemesSupported
WAIS
```

Wide Area Information Server (WAIS) protocol.

- FILE

```java
public static final
ReferenceUriSchemesSupported
FILE
```

Host-specific file names.

---

#### Field Detail

FTP

```java
public static final
ReferenceUriSchemesSupported
FTP
```

File Transfer Protocol (FTP).

---

#### FTP

public static final

ReferenceUriSchemesSupported

FTP

File Transfer Protocol (FTP).

HTTP

```java
public static final
ReferenceUriSchemesSupported
HTTP
```

HyperText Transfer Protocol (HTTP).

---

#### HTTP

public static final

ReferenceUriSchemesSupported

HTTP

HyperText Transfer Protocol (HTTP).

HTTPS

```java
public static final
ReferenceUriSchemesSupported
HTTPS
```

Secure HyperText Transfer Protocol (HTTPS).

---

#### HTTPS

public static final

ReferenceUriSchemesSupported

HTTPS

Secure HyperText Transfer Protocol (HTTPS).

GOPHER

```java
public static final
ReferenceUriSchemesSupported
GOPHER
```

Gopher Protocol.

---

#### GOPHER

public static final

ReferenceUriSchemesSupported

GOPHER

Gopher Protocol.

NEWS

```java
public static final
ReferenceUriSchemesSupported
NEWS
```

USENET news.

---

#### NEWS

public static final

ReferenceUriSchemesSupported

NEWS

USENET news.

NNTP

```java
public static final
ReferenceUriSchemesSupported
NNTP
```

USENET news using Network News Transfer Protocol (NNTP).

---

#### NNTP

public static final

ReferenceUriSchemesSupported

NNTP

USENET news using Network News Transfer Protocol (NNTP).

WAIS

```java
public static final
ReferenceUriSchemesSupported
WAIS
```

Wide Area Information Server (WAIS) protocol.

---

#### WAIS

public static final

ReferenceUriSchemesSupported

WAIS

Wide Area Information Server (WAIS) protocol.

FILE

```java
public static final
ReferenceUriSchemesSupported
FILE
```

Host-specific file names.

---

#### FILE

public static final

ReferenceUriSchemesSupported

FILE

Host-specific file names.

Constructor Detail

- ReferenceUriSchemesSupported

```java
protected ReferenceUriSchemesSupported​(int value)
```

Construct a new reference

URI

scheme enumeration value with the
given integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

ReferenceUriSchemesSupported

```java
protected ReferenceUriSchemesSupported​(int value)
```

Construct a new reference

URI

scheme enumeration value with the
given integer value.

**Parameters:** value

- Integer value

---

#### ReferenceUriSchemesSupported

protected ReferenceUriSchemesSupported​(int value)

Construct a new reference

URI

scheme enumeration value with the
given integer value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

ReferenceUriSchemesSupported

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

ReferenceUriSchemesSupported

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category is class

ReferenceUriSchemesSupported

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category name is

"reference-uri-schemes-supported"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

ReferenceUriSchemesSupported

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

---

#### getStringTable

protected

String

[] getStringTable()

Returns the string table for class

ReferenceUriSchemesSupported

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

ReferenceUriSchemesSupported

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

---

#### getEnumValueTable

protected

EnumSyntax

[] getEnumValueTable()

Returns the enumeration value table for class

ReferenceUriSchemesSupported

.

getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category is class

ReferenceUriSchemesSupported

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

---

#### getCategory

public final

Class

<? extends

Attribute

> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category is class

ReferenceUriSchemesSupported

itself.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category is class

ReferenceUriSchemesSupported

itself.

getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category name is

"reference-uri-schemes-supported"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### getName

public final

String

getName()

Get the name of the category of which this attribute value is an
instance.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category name is

"reference-uri-schemes-supported"

.

For class

ReferenceUriSchemesSupported

and any vendor-defined
subclasses, the category name is

"reference-uri-schemes-supported"

.

---

