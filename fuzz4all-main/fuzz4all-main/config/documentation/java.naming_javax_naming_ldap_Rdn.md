# Class Rdn

**Source:** `java.naming\javax\naming\ldap\Rdn.html`

### Class Description

```java
public class
Rdn

extends
Object

implements
Serializable
,
Comparable
<
Object
>
```

This class represents a relative distinguished name, or RDN, which is a
component of a distinguished name as specified by

RFC 2253

.
An example of an RDN is "OU=Sales+CN=J.Smith". In this example,
the RDN consist of multiple attribute type/value pairs. The
RDN is parsed as described in the class description for

LdapName

.

The Rdn class represents an RDN as attribute type/value mappings,
which can be viewed using

Attributes

.
In addition, it contains convenience methods that allow easy retrieval
of type and value when the Rdn consist of a single type/value pair,
which is how it appears in a typical usage.
It also contains helper methods that allow escaping of the unformatted
attribute value and unescaping of the value formatted according to the
escaping syntax defined in RFC2253. For methods that take or return
attribute value as an Object, the value is either a String
(in unescaped form) or a byte array.

Rdn

will properly parse all valid RDNs, but
does not attempt to detect all possible violations when parsing
invalid RDNs. It is "generous" in accepting invalid RDNs.
The "validity" of a name is determined ultimately when it
is supplied to an LDAP server, which may accept or
reject the name based on factors such as its schema information
and interoperability considerations.

The following code example shows how to construct an Rdn using the
constructor that takes type and value as arguments:

```java
Rdn rdn = new Rdn("cn", "Juicy, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

. The

unescapeValue()

method can be
used to unescape the escaped comma resulting in the original
value

"Juicy, Fruit"

. The

escapeValue()

method adds the escape back preceding the comma.

This class can be instantiated by a string representation
of the RDN defined in RFC 2253 as shown in the following code example:

```java
Rdn rdn = new Rdn("cn=Juicy\\, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

.

Concurrent multithreaded read-only access of an instance of

Rdn

need not be synchronized.

Unless otherwise noted, the behavior of passing a null argument
to a constructor or method in this class will cause NullPointerException
to be thrown.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Object

>

---

### Field Details

*No entries found.*

### Constructor Details

#### public Rdn​(
Attributes
attrSet)
throws
InvalidNameException

Constructs an Rdn from the given attribute set. See

Attributes

.

The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

**Parameters:**
- attrSet

- The non-null and non-empty attributes containing
type/value mappings.

**Throws:**
- InvalidNameException

- If contents of

attrSet

cannot
be used to construct a valid RDN.

---

#### public Rdn​(
String
rdnString)
throws
InvalidNameException

Constructs an Rdn from the given string.
This constructor takes a string formatted according to the rules
defined in

RFC 2253

and described in the class description for

LdapName

.

**Parameters:**
- rdnString

- The non-null and non-empty RFC2253 formatted string.

**Throws:**
- InvalidNameException

- If a syntax error occurs during
parsing of the rdnString.

---

#### public Rdn​(
Rdn
rdn)

Constructs an Rdn from the given

rdn

.
The contents of the

rdn

are simply copied into the newly
created Rdn.

**Parameters:**
- rdn

- The non-null Rdn to be copied.

---

#### public Rdn​(
String
type,

Object
value)
throws
InvalidNameException

Constructs an Rdn from the given attribute type and
value.
The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

**Parameters:**
- type

- The non-null and non-empty string attribute type.
- value

- The non-null and non-empty attribute value.

**Throws:**
- InvalidNameException

- If type/value cannot be used to
construct a valid RDN.

**See Also:**
- toString()

---

### Method Details

#### public
Object
getValue()

Retrieves one of this Rdn's value.
This is a convenience method for obtaining the value,
when the RDN contains a single type and value mapping,
which is the common RDN usage.

For a multi-valued RDN, this method returns value corresponding
to the type returned by

getType()

method.

**Returns:**
- The non-null attribute value.

---

#### public
String
getType()

Retrieves one of this Rdn's type.
This is a convenience method for obtaining the type,
when the RDN contains a single type and value mapping,
which is the common RDN usage.

For a multi-valued RDN, the type/value pairs have
no specific order defined on them. In that case, this method
returns type of one of the type/value pairs.
The

getValue()

method returns the
value corresponding to the type returned by this method.

**Returns:**
- The non-null attribute type.

---

#### public
String
toString()

Returns this Rdn as a string represented in a format defined by

RFC 2253

and described
in the class description for

LdapName

.

**Overrides:**
- toString

in class

Object

**Returns:**
- The string representation of the Rdn.

---

#### public int compareTo​(
Object
obj)

Compares this Rdn with the specified Object for order.
Returns a negative integer, zero, or a positive integer as this
Rdn is less than, equal to, or greater than the given Object.

If obj is null or not an instance of Rdn, ClassCastException
is thrown.

The attribute type and value pairs of the RDNs are lined up
against each other and compared lexicographically. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

**Specified by:**
- compareTo

in interface

Comparable

<

Object

>

**Parameters:**
- obj

- The non-null object to compare against.

**Returns:**
- A negative integer, zero, or a positive integer as this Rdn
is less than, equal to, or greater than the given Object.

**Throws:**
- ClassCastException

- if obj is null or not a Rdn.

---

#### public boolean equals​(
Object
obj)

Compares the specified Object with this Rdn for equality.
Returns true if the given object is also a Rdn and the two Rdns
represent the same attribute type and value mappings. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

Type and value equality matching is done as below:

- The types are compared for equality with their case ignored.

String values with different but equivalent usage of quoting,
escaping, or UTF8-hex-encoding are considered equal.
The case of the values is ignored during the comparison.

If obj is null or not an instance of Rdn, false is returned.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- object to be compared for equality with this Rdn.

**Returns:**
- true if the specified object is equal to this Rdn.

**See Also:**
- hashCode()

---

#### public int hashCode()

Returns the hash code of this RDN. Two RDNs that are
equal (according to the equals method) will have the same
hash code.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- An int representing the hash code of this Rdn.

**See Also:**
- equals(java.lang.Object)

---

#### public
Attributes
toAttributes()

Retrieves the

Attributes

view of the type/value mappings contained in this Rdn.

**Returns:**
- The non-null attributes containing the type/value
mappings of this Rdn.

---

#### public int size()

Retrieves the number of attribute type/value pairs in this Rdn.

**Returns:**
- The non-negative number of type/value pairs in this Rdn.

---

#### public static
String
escapeValue​(
Object
val)

Given the value of an attribute, returns a string escaped according
to the rules specified in

RFC 2253

.

For example, if the val is "Sue, Grabbit and Runn", the escaped
value returned by this method is "Sue\, Grabbit and Runn".

A string value is represented as a String and binary value
as a byte array.

**Parameters:**
- val

- The non-null object to be escaped.

**Returns:**
- Escaped string value.

**Throws:**
- ClassCastException

- if val is not a String or byte array.

---

#### public static
Object
unescapeValue​(
String
val)

Given an attribute value string formatted according to the rules
specified in

RFC 2253

,
returns the unformatted value. Escapes and quotes are
stripped away, and hex-encoded UTF-8 is converted to equivalent
UTF-16 characters. Returns a string value as a String, and a
binary value as a byte array.

Legal and illegal values are defined in RFC 2253.
This method is generous in accepting the values and does not
catch all illegal values.
Therefore, passing in an illegal value might not necessarily
trigger an

IllegalArgumentException

.

**Parameters:**
- val

- The non-null string to be unescaped.

**Returns:**
- Unescaped value.

**Throws:**
- IllegalArgumentException

- When an Illegal value
is provided.

---

### Additional Sections

#### Class Rdn

java.lang.Object

- javax.naming.ldap.Rdn

javax.naming.ldap.Rdn

**All Implemented Interfaces:** Serializable

,

Comparable

<

Object

>

```java
public class
Rdn

extends
Object

implements
Serializable
,
Comparable
<
Object
>
```

This class represents a relative distinguished name, or RDN, which is a
component of a distinguished name as specified by

RFC 2253

.
An example of an RDN is "OU=Sales+CN=J.Smith". In this example,
the RDN consist of multiple attribute type/value pairs. The
RDN is parsed as described in the class description for

LdapName

.

The Rdn class represents an RDN as attribute type/value mappings,
which can be viewed using

Attributes

.
In addition, it contains convenience methods that allow easy retrieval
of type and value when the Rdn consist of a single type/value pair,
which is how it appears in a typical usage.
It also contains helper methods that allow escaping of the unformatted
attribute value and unescaping of the value formatted according to the
escaping syntax defined in RFC2253. For methods that take or return
attribute value as an Object, the value is either a String
(in unescaped form) or a byte array.

Rdn

will properly parse all valid RDNs, but
does not attempt to detect all possible violations when parsing
invalid RDNs. It is "generous" in accepting invalid RDNs.
The "validity" of a name is determined ultimately when it
is supplied to an LDAP server, which may accept or
reject the name based on factors such as its schema information
and interoperability considerations.

The following code example shows how to construct an Rdn using the
constructor that takes type and value as arguments:

```java
Rdn rdn = new Rdn("cn", "Juicy, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

. The

unescapeValue()

method can be
used to unescape the escaped comma resulting in the original
value

"Juicy, Fruit"

. The

escapeValue()

method adds the escape back preceding the comma.

This class can be instantiated by a string representation
of the RDN defined in RFC 2253 as shown in the following code example:

```java
Rdn rdn = new Rdn("cn=Juicy\\, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

.

Concurrent multithreaded read-only access of an instance of

Rdn

need not be synchronized.

Unless otherwise noted, the behavior of passing a null argument
to a constructor or method in this class will cause NullPointerException
to be thrown.

**Since:** 1.5
**See Also:** Serialized Form

public class

Rdn

extends

Object

implements

Serializable

,

Comparable

<

Object

>

This class represents a relative distinguished name, or RDN, which is a
component of a distinguished name as specified by

RFC 2253

.
An example of an RDN is "OU=Sales+CN=J.Smith". In this example,
the RDN consist of multiple attribute type/value pairs. The
RDN is parsed as described in the class description for

LdapName

.

The Rdn class represents an RDN as attribute type/value mappings,
which can be viewed using

Attributes

.
In addition, it contains convenience methods that allow easy retrieval
of type and value when the Rdn consist of a single type/value pair,
which is how it appears in a typical usage.
It also contains helper methods that allow escaping of the unformatted
attribute value and unescaping of the value formatted according to the
escaping syntax defined in RFC2253. For methods that take or return
attribute value as an Object, the value is either a String
(in unescaped form) or a byte array.

Rdn

will properly parse all valid RDNs, but
does not attempt to detect all possible violations when parsing
invalid RDNs. It is "generous" in accepting invalid RDNs.
The "validity" of a name is determined ultimately when it
is supplied to an LDAP server, which may accept or
reject the name based on factors such as its schema information
and interoperability considerations.

The following code example shows how to construct an Rdn using the
constructor that takes type and value as arguments:

```java
Rdn rdn = new Rdn("cn", "Juicy, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

. The

unescapeValue()

method can be
used to unescape the escaped comma resulting in the original
value

"Juicy, Fruit"

. The

escapeValue()

method adds the escape back preceding the comma.

This class can be instantiated by a string representation
of the RDN defined in RFC 2253 as shown in the following code example:

```java
Rdn rdn = new Rdn("cn=Juicy\\, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

.

Concurrent multithreaded read-only access of an instance of

Rdn

need not be synchronized.

Unless otherwise noted, the behavior of passing a null argument
to a constructor or method in this class will cause NullPointerException
to be thrown.

The Rdn class represents an RDN as attribute type/value mappings,
which can be viewed using

Attributes

.
In addition, it contains convenience methods that allow easy retrieval
of type and value when the Rdn consist of a single type/value pair,
which is how it appears in a typical usage.
It also contains helper methods that allow escaping of the unformatted
attribute value and unescaping of the value formatted according to the
escaping syntax defined in RFC2253. For methods that take or return
attribute value as an Object, the value is either a String
(in unescaped form) or a byte array.

Rdn

will properly parse all valid RDNs, but
does not attempt to detect all possible violations when parsing
invalid RDNs. It is "generous" in accepting invalid RDNs.
The "validity" of a name is determined ultimately when it
is supplied to an LDAP server, which may accept or
reject the name based on factors such as its schema information
and interoperability considerations.

The following code example shows how to construct an Rdn using the
constructor that takes type and value as arguments:

```java
Rdn rdn = new Rdn("cn", "Juicy, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

. The

unescapeValue()

method can be
used to unescape the escaped comma resulting in the original
value

"Juicy, Fruit"

. The

escapeValue()

method adds the escape back preceding the comma.

This class can be instantiated by a string representation
of the RDN defined in RFC 2253 as shown in the following code example:

```java
Rdn rdn = new Rdn("cn=Juicy\\, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

.

Concurrent multithreaded read-only access of an instance of

Rdn

need not be synchronized.

Unless otherwise noted, the behavior of passing a null argument
to a constructor or method in this class will cause NullPointerException
to be thrown.

Rdn

will properly parse all valid RDNs, but
does not attempt to detect all possible violations when parsing
invalid RDNs. It is "generous" in accepting invalid RDNs.
The "validity" of a name is determined ultimately when it
is supplied to an LDAP server, which may accept or
reject the name based on factors such as its schema information
and interoperability considerations.

The following code example shows how to construct an Rdn using the
constructor that takes type and value as arguments:

```java
Rdn rdn = new Rdn("cn", "Juicy, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

. The

unescapeValue()

method can be
used to unescape the escaped comma resulting in the original
value

"Juicy, Fruit"

. The

escapeValue()

method adds the escape back preceding the comma.

This class can be instantiated by a string representation
of the RDN defined in RFC 2253 as shown in the following code example:

```java
Rdn rdn = new Rdn("cn=Juicy\\, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

.

Concurrent multithreaded read-only access of an instance of

Rdn

need not be synchronized.

Unless otherwise noted, the behavior of passing a null argument
to a constructor or method in this class will cause NullPointerException
to be thrown.

The following code example shows how to construct an Rdn using the
constructor that takes type and value as arguments:

```java
Rdn rdn = new Rdn("cn", "Juicy, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

. The

unescapeValue()

method can be
used to unescape the escaped comma resulting in the original
value

"Juicy, Fruit"

. The

escapeValue()

method adds the escape back preceding the comma.

This class can be instantiated by a string representation
of the RDN defined in RFC 2253 as shown in the following code example:

```java
Rdn rdn = new Rdn("cn=Juicy\\, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

.

Concurrent multithreaded read-only access of an instance of

Rdn

need not be synchronized.

Unless otherwise noted, the behavior of passing a null argument
to a constructor or method in this class will cause NullPointerException
to be thrown.

Rdn rdn = new Rdn("cn", "Juicy, Fruit");
System.out.println(rdn.toString());

This class can be instantiated by a string representation
of the RDN defined in RFC 2253 as shown in the following code example:

```java
Rdn rdn = new Rdn("cn=Juicy\\, Fruit");
System.out.println(rdn.toString());
```

The last line will print

cn=Juicy\, Fruit

.

Concurrent multithreaded read-only access of an instance of

Rdn

need not be synchronized.

Unless otherwise noted, the behavior of passing a null argument
to a constructor or method in this class will cause NullPointerException
to be thrown.

Rdn rdn = new Rdn("cn=Juicy\\, Fruit");
System.out.println(rdn.toString());

Concurrent multithreaded read-only access of an instance of

Rdn

need not be synchronized.

Unless otherwise noted, the behavior of passing a null argument
to a constructor or method in this class will cause NullPointerException
to be thrown.

Unless otherwise noted, the behavior of passing a null argument
to a constructor or method in this class will cause NullPointerException
to be thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Rdn

​(

String

rdnString)

Constructs an Rdn from the given string.

Rdn

​(

String

type,

Object

value)

Constructs an Rdn from the given attribute type and
value.

Rdn

​(

Attributes

attrSet)

Constructs an Rdn from the given attribute set.

Rdn

​(

Rdn

rdn)

Constructs an Rdn from the given

rdn

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

compareTo

​(

Object

obj)

Compares this Rdn with the specified Object for order.

boolean

equals

​(

Object

obj)

Compares the specified Object with this Rdn for equality.

static

String

escapeValue

​(

Object

val)

Given the value of an attribute, returns a string escaped according
to the rules specified in

RFC 2253

.

String

getType

()

Retrieves one of this Rdn's type.

Object

getValue

()

Retrieves one of this Rdn's value.

int

hashCode

()

Returns the hash code of this RDN.

int

size

()

Retrieves the number of attribute type/value pairs in this Rdn.

Attributes

toAttributes

()

Retrieves the

Attributes

view of the type/value mappings contained in this Rdn.

String

toString

()

Returns this Rdn as a string represented in a format defined by

RFC 2253

and described
in the class description for

LdapName

.

static

Object

unescapeValue

​(

String

val)

Given an attribute value string formatted according to the rules
specified in

RFC 2253

,
returns the unformatted value.

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

Rdn

​(

String

rdnString)

Constructs an Rdn from the given string.

Rdn

​(

String

type,

Object

value)

Constructs an Rdn from the given attribute type and
value.

Rdn

​(

Attributes

attrSet)

Constructs an Rdn from the given attribute set.

Rdn

​(

Rdn

rdn)

Constructs an Rdn from the given

rdn

.

---

#### Constructor Summary

Constructs an Rdn from the given string.

Constructs an Rdn from the given attribute type and
value.

Constructs an Rdn from the given attribute set.

Constructs an Rdn from the given

rdn

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

compareTo

​(

Object

obj)

Compares this Rdn with the specified Object for order.

boolean

equals

​(

Object

obj)

Compares the specified Object with this Rdn for equality.

static

String

escapeValue

​(

Object

val)

Given the value of an attribute, returns a string escaped according
to the rules specified in

RFC 2253

.

String

getType

()

Retrieves one of this Rdn's type.

Object

getValue

()

Retrieves one of this Rdn's value.

int

hashCode

()

Returns the hash code of this RDN.

int

size

()

Retrieves the number of attribute type/value pairs in this Rdn.

Attributes

toAttributes

()

Retrieves the

Attributes

view of the type/value mappings contained in this Rdn.

String

toString

()

Returns this Rdn as a string represented in a format defined by

RFC 2253

and described
in the class description for

LdapName

.

static

Object

unescapeValue

​(

String

val)

Given an attribute value string formatted according to the rules
specified in

RFC 2253

,
returns the unformatted value.

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

Compares this Rdn with the specified Object for order.

Compares the specified Object with this Rdn for equality.

Given the value of an attribute, returns a string escaped according
to the rules specified in

RFC 2253

.

Retrieves one of this Rdn's type.

Retrieves one of this Rdn's value.

Returns the hash code of this RDN.

Retrieves the number of attribute type/value pairs in this Rdn.

Retrieves the

Attributes

view of the type/value mappings contained in this Rdn.

Returns this Rdn as a string represented in a format defined by

RFC 2253

and described
in the class description for

LdapName

.

Given an attribute value string formatted according to the rules
specified in

RFC 2253

,
returns the unformatted value.

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

- Rdn

```java
public Rdn​(
Attributes
attrSet)
throws
InvalidNameException
```

Constructs an Rdn from the given attribute set. See

Attributes

.

The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

**Parameters:** attrSet

- The non-null and non-empty attributes containing
type/value mappings.
**Throws:** InvalidNameException

- If contents of

attrSet

cannot
be used to construct a valid RDN.

- Rdn

```java
public Rdn​(
String
rdnString)
throws
InvalidNameException
```

Constructs an Rdn from the given string.
This constructor takes a string formatted according to the rules
defined in

RFC 2253

and described in the class description for

LdapName

.

**Parameters:** rdnString

- The non-null and non-empty RFC2253 formatted string.
**Throws:** InvalidNameException

- If a syntax error occurs during
parsing of the rdnString.

- Rdn

```java
public Rdn​(
Rdn
rdn)
```

Constructs an Rdn from the given

rdn

.
The contents of the

rdn

are simply copied into the newly
created Rdn.

**Parameters:** rdn

- The non-null Rdn to be copied.

- Rdn

```java
public Rdn​(
String
type,

Object
value)
throws
InvalidNameException
```

Constructs an Rdn from the given attribute type and
value.
The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

**Parameters:** type

- The non-null and non-empty string attribute type.
**Parameters:** value

- The non-null and non-empty attribute value.
**Throws:** InvalidNameException

- If type/value cannot be used to
construct a valid RDN.
**See Also:** toString()

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
public
Object
getValue()
```

Retrieves one of this Rdn's value.
This is a convenience method for obtaining the value,
when the RDN contains a single type and value mapping,
which is the common RDN usage.

For a multi-valued RDN, this method returns value corresponding
to the type returned by

getType()

method.

**Returns:** The non-null attribute value.

- getType

```java
public
String
getType()
```

Retrieves one of this Rdn's type.
This is a convenience method for obtaining the type,
when the RDN contains a single type and value mapping,
which is the common RDN usage.

For a multi-valued RDN, the type/value pairs have
no specific order defined on them. In that case, this method
returns type of one of the type/value pairs.
The

getValue()

method returns the
value corresponding to the type returned by this method.

**Returns:** The non-null attribute type.

- toString

```java
public
String
toString()
```

Returns this Rdn as a string represented in a format defined by

RFC 2253

and described
in the class description for

LdapName

.

**Overrides:** toString

in class

Object
**Returns:** The string representation of the Rdn.

- compareTo

```java
public int compareTo​(
Object
obj)
```

Compares this Rdn with the specified Object for order.
Returns a negative integer, zero, or a positive integer as this
Rdn is less than, equal to, or greater than the given Object.

If obj is null or not an instance of Rdn, ClassCastException
is thrown.

The attribute type and value pairs of the RDNs are lined up
against each other and compared lexicographically. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- The non-null object to compare against.
**Returns:** A negative integer, zero, or a positive integer as this Rdn
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- if obj is null or not a Rdn.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified Object with this Rdn for equality.
Returns true if the given object is also a Rdn and the two Rdns
represent the same attribute type and value mappings. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

Type and value equality matching is done as below:

- The types are compared for equality with their case ignored.

String values with different but equivalent usage of quoting,
escaping, or UTF8-hex-encoding are considered equal.
The case of the values is ignored during the comparison.

If obj is null or not an instance of Rdn, false is returned.

**Overrides:** equals

in class

Object
**Parameters:** obj

- object to be compared for equality with this Rdn.
**Returns:** true if the specified object is equal to this Rdn.
**See Also:** hashCode()

- hashCode

```java
public int hashCode()
```

Returns the hash code of this RDN. Two RDNs that are
equal (according to the equals method) will have the same
hash code.

**Overrides:** hashCode

in class

Object
**Returns:** An int representing the hash code of this Rdn.
**See Also:** equals(java.lang.Object)

- toAttributes

```java
public
Attributes
toAttributes()
```

Retrieves the

Attributes

view of the type/value mappings contained in this Rdn.

**Returns:** The non-null attributes containing the type/value
mappings of this Rdn.

- size

```java
public int size()
```

Retrieves the number of attribute type/value pairs in this Rdn.

**Returns:** The non-negative number of type/value pairs in this Rdn.

- escapeValue

```java
public static
String
escapeValue​(
Object
val)
```

Given the value of an attribute, returns a string escaped according
to the rules specified in

RFC 2253

.

For example, if the val is "Sue, Grabbit and Runn", the escaped
value returned by this method is "Sue\, Grabbit and Runn".

A string value is represented as a String and binary value
as a byte array.

**Parameters:** val

- The non-null object to be escaped.
**Returns:** Escaped string value.
**Throws:** ClassCastException

- if val is not a String or byte array.

- unescapeValue

```java
public static
Object
unescapeValue​(
String
val)
```

Given an attribute value string formatted according to the rules
specified in

RFC 2253

,
returns the unformatted value. Escapes and quotes are
stripped away, and hex-encoded UTF-8 is converted to equivalent
UTF-16 characters. Returns a string value as a String, and a
binary value as a byte array.

Legal and illegal values are defined in RFC 2253.
This method is generous in accepting the values and does not
catch all illegal values.
Therefore, passing in an illegal value might not necessarily
trigger an

IllegalArgumentException

.

**Parameters:** val

- The non-null string to be unescaped.
**Returns:** Unescaped value.
**Throws:** IllegalArgumentException

- When an Illegal value
is provided.

Constructor Detail

- Rdn

```java
public Rdn​(
Attributes
attrSet)
throws
InvalidNameException
```

Constructs an Rdn from the given attribute set. See

Attributes

.

The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

**Parameters:** attrSet

- The non-null and non-empty attributes containing
type/value mappings.
**Throws:** InvalidNameException

- If contents of

attrSet

cannot
be used to construct a valid RDN.

- Rdn

```java
public Rdn​(
String
rdnString)
throws
InvalidNameException
```

Constructs an Rdn from the given string.
This constructor takes a string formatted according to the rules
defined in

RFC 2253

and described in the class description for

LdapName

.

**Parameters:** rdnString

- The non-null and non-empty RFC2253 formatted string.
**Throws:** InvalidNameException

- If a syntax error occurs during
parsing of the rdnString.

- Rdn

```java
public Rdn​(
Rdn
rdn)
```

Constructs an Rdn from the given

rdn

.
The contents of the

rdn

are simply copied into the newly
created Rdn.

**Parameters:** rdn

- The non-null Rdn to be copied.

- Rdn

```java
public Rdn​(
String
type,

Object
value)
throws
InvalidNameException
```

Constructs an Rdn from the given attribute type and
value.
The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

**Parameters:** type

- The non-null and non-empty string attribute type.
**Parameters:** value

- The non-null and non-empty attribute value.
**Throws:** InvalidNameException

- If type/value cannot be used to
construct a valid RDN.
**See Also:** toString()

---

#### Constructor Detail

Rdn

```java
public Rdn​(
Attributes
attrSet)
throws
InvalidNameException
```

Constructs an Rdn from the given attribute set. See

Attributes

.

The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

**Parameters:** attrSet

- The non-null and non-empty attributes containing
type/value mappings.
**Throws:** InvalidNameException

- If contents of

attrSet

cannot
be used to construct a valid RDN.

---

#### Rdn

public Rdn​(

Attributes

attrSet)
throws

InvalidNameException

Constructs an Rdn from the given attribute set. See

Attributes

.

The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

Rdn

```java
public Rdn​(
String
rdnString)
throws
InvalidNameException
```

Constructs an Rdn from the given string.
This constructor takes a string formatted according to the rules
defined in

RFC 2253

and described in the class description for

LdapName

.

**Parameters:** rdnString

- The non-null and non-empty RFC2253 formatted string.
**Throws:** InvalidNameException

- If a syntax error occurs during
parsing of the rdnString.

---

#### Rdn

public Rdn​(

String

rdnString)
throws

InvalidNameException

Constructs an Rdn from the given string.
This constructor takes a string formatted according to the rules
defined in

RFC 2253

and described in the class description for

LdapName

.

Rdn

```java
public Rdn​(
Rdn
rdn)
```

Constructs an Rdn from the given

rdn

.
The contents of the

rdn

are simply copied into the newly
created Rdn.

**Parameters:** rdn

- The non-null Rdn to be copied.

---

#### Rdn

public Rdn​(

Rdn

rdn)

Constructs an Rdn from the given

rdn

.
The contents of the

rdn

are simply copied into the newly
created Rdn.

Rdn

```java
public Rdn​(
String
type,

Object
value)
throws
InvalidNameException
```

Constructs an Rdn from the given attribute type and
value.
The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

**Parameters:** type

- The non-null and non-empty string attribute type.
**Parameters:** value

- The non-null and non-empty attribute value.
**Throws:** InvalidNameException

- If type/value cannot be used to
construct a valid RDN.
**See Also:** toString()

---

#### Rdn

public Rdn​(

String

type,

Object

value)
throws

InvalidNameException

Constructs an Rdn from the given attribute type and
value.
The string attribute values are not interpreted as

RFC 2253

formatted RDN strings. That is, the values are used
literally (not parsed) and assumed to be unescaped.

Method Detail

- getValue

```java
public
Object
getValue()
```

Retrieves one of this Rdn's value.
This is a convenience method for obtaining the value,
when the RDN contains a single type and value mapping,
which is the common RDN usage.

For a multi-valued RDN, this method returns value corresponding
to the type returned by

getType()

method.

**Returns:** The non-null attribute value.

- getType

```java
public
String
getType()
```

Retrieves one of this Rdn's type.
This is a convenience method for obtaining the type,
when the RDN contains a single type and value mapping,
which is the common RDN usage.

For a multi-valued RDN, the type/value pairs have
no specific order defined on them. In that case, this method
returns type of one of the type/value pairs.
The

getValue()

method returns the
value corresponding to the type returned by this method.

**Returns:** The non-null attribute type.

- toString

```java
public
String
toString()
```

Returns this Rdn as a string represented in a format defined by

RFC 2253

and described
in the class description for

LdapName

.

**Overrides:** toString

in class

Object
**Returns:** The string representation of the Rdn.

- compareTo

```java
public int compareTo​(
Object
obj)
```

Compares this Rdn with the specified Object for order.
Returns a negative integer, zero, or a positive integer as this
Rdn is less than, equal to, or greater than the given Object.

If obj is null or not an instance of Rdn, ClassCastException
is thrown.

The attribute type and value pairs of the RDNs are lined up
against each other and compared lexicographically. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- The non-null object to compare against.
**Returns:** A negative integer, zero, or a positive integer as this Rdn
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- if obj is null or not a Rdn.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified Object with this Rdn for equality.
Returns true if the given object is also a Rdn and the two Rdns
represent the same attribute type and value mappings. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

Type and value equality matching is done as below:

- The types are compared for equality with their case ignored.

String values with different but equivalent usage of quoting,
escaping, or UTF8-hex-encoding are considered equal.
The case of the values is ignored during the comparison.

If obj is null or not an instance of Rdn, false is returned.

**Overrides:** equals

in class

Object
**Parameters:** obj

- object to be compared for equality with this Rdn.
**Returns:** true if the specified object is equal to this Rdn.
**See Also:** hashCode()

- hashCode

```java
public int hashCode()
```

Returns the hash code of this RDN. Two RDNs that are
equal (according to the equals method) will have the same
hash code.

**Overrides:** hashCode

in class

Object
**Returns:** An int representing the hash code of this Rdn.
**See Also:** equals(java.lang.Object)

- toAttributes

```java
public
Attributes
toAttributes()
```

Retrieves the

Attributes

view of the type/value mappings contained in this Rdn.

**Returns:** The non-null attributes containing the type/value
mappings of this Rdn.

- size

```java
public int size()
```

Retrieves the number of attribute type/value pairs in this Rdn.

**Returns:** The non-negative number of type/value pairs in this Rdn.

- escapeValue

```java
public static
String
escapeValue​(
Object
val)
```

Given the value of an attribute, returns a string escaped according
to the rules specified in

RFC 2253

.

For example, if the val is "Sue, Grabbit and Runn", the escaped
value returned by this method is "Sue\, Grabbit and Runn".

A string value is represented as a String and binary value
as a byte array.

**Parameters:** val

- The non-null object to be escaped.
**Returns:** Escaped string value.
**Throws:** ClassCastException

- if val is not a String or byte array.

- unescapeValue

```java
public static
Object
unescapeValue​(
String
val)
```

Given an attribute value string formatted according to the rules
specified in

RFC 2253

,
returns the unformatted value. Escapes and quotes are
stripped away, and hex-encoded UTF-8 is converted to equivalent
UTF-16 characters. Returns a string value as a String, and a
binary value as a byte array.

Legal and illegal values are defined in RFC 2253.
This method is generous in accepting the values and does not
catch all illegal values.
Therefore, passing in an illegal value might not necessarily
trigger an

IllegalArgumentException

.

**Parameters:** val

- The non-null string to be unescaped.
**Returns:** Unescaped value.
**Throws:** IllegalArgumentException

- When an Illegal value
is provided.

---

#### Method Detail

getValue

```java
public
Object
getValue()
```

Retrieves one of this Rdn's value.
This is a convenience method for obtaining the value,
when the RDN contains a single type and value mapping,
which is the common RDN usage.

For a multi-valued RDN, this method returns value corresponding
to the type returned by

getType()

method.

**Returns:** The non-null attribute value.

---

#### getValue

public

Object

getValue()

Retrieves one of this Rdn's value.
This is a convenience method for obtaining the value,
when the RDN contains a single type and value mapping,
which is the common RDN usage.

For a multi-valued RDN, this method returns value corresponding
to the type returned by

getType()

method.

For a multi-valued RDN, this method returns value corresponding
to the type returned by

getType()

method.

getType

```java
public
String
getType()
```

Retrieves one of this Rdn's type.
This is a convenience method for obtaining the type,
when the RDN contains a single type and value mapping,
which is the common RDN usage.

For a multi-valued RDN, the type/value pairs have
no specific order defined on them. In that case, this method
returns type of one of the type/value pairs.
The

getValue()

method returns the
value corresponding to the type returned by this method.

**Returns:** The non-null attribute type.

---

#### getType

public

String

getType()

Retrieves one of this Rdn's type.
This is a convenience method for obtaining the type,
when the RDN contains a single type and value mapping,
which is the common RDN usage.

For a multi-valued RDN, the type/value pairs have
no specific order defined on them. In that case, this method
returns type of one of the type/value pairs.
The

getValue()

method returns the
value corresponding to the type returned by this method.

For a multi-valued RDN, the type/value pairs have
no specific order defined on them. In that case, this method
returns type of one of the type/value pairs.
The

getValue()

method returns the
value corresponding to the type returned by this method.

toString

```java
public
String
toString()
```

Returns this Rdn as a string represented in a format defined by

RFC 2253

and described
in the class description for

LdapName

.

**Overrides:** toString

in class

Object
**Returns:** The string representation of the Rdn.

---

#### toString

public

String

toString()

Returns this Rdn as a string represented in a format defined by

RFC 2253

and described
in the class description for

LdapName

.

compareTo

```java
public int compareTo​(
Object
obj)
```

Compares this Rdn with the specified Object for order.
Returns a negative integer, zero, or a positive integer as this
Rdn is less than, equal to, or greater than the given Object.

If obj is null or not an instance of Rdn, ClassCastException
is thrown.

The attribute type and value pairs of the RDNs are lined up
against each other and compared lexicographically. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- The non-null object to compare against.
**Returns:** A negative integer, zero, or a positive integer as this Rdn
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- if obj is null or not a Rdn.

---

#### compareTo

public int compareTo​(

Object

obj)

Compares this Rdn with the specified Object for order.
Returns a negative integer, zero, or a positive integer as this
Rdn is less than, equal to, or greater than the given Object.

If obj is null or not an instance of Rdn, ClassCastException
is thrown.

The attribute type and value pairs of the RDNs are lined up
against each other and compared lexicographically. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

If obj is null or not an instance of Rdn, ClassCastException
is thrown.

The attribute type and value pairs of the RDNs are lined up
against each other and compared lexicographically. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

The attribute type and value pairs of the RDNs are lined up
against each other and compared lexicographically. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified Object with this Rdn for equality.
Returns true if the given object is also a Rdn and the two Rdns
represent the same attribute type and value mappings. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

Type and value equality matching is done as below:

- The types are compared for equality with their case ignored.

String values with different but equivalent usage of quoting,
escaping, or UTF8-hex-encoding are considered equal.
The case of the values is ignored during the comparison.

If obj is null or not an instance of Rdn, false is returned.

**Overrides:** equals

in class

Object
**Parameters:** obj

- object to be compared for equality with this Rdn.
**Returns:** true if the specified object is equal to this Rdn.
**See Also:** hashCode()

---

#### equals

public boolean equals​(

Object

obj)

Compares the specified Object with this Rdn for equality.
Returns true if the given object is also a Rdn and the two Rdns
represent the same attribute type and value mappings. The order of
components in multi-valued Rdns (such as "ou=Sales+cn=Bob") is not
significant.

Type and value equality matching is done as below:

- The types are compared for equality with their case ignored.

String values with different but equivalent usage of quoting,
escaping, or UTF8-hex-encoding are considered equal.
The case of the values is ignored during the comparison.

If obj is null or not an instance of Rdn, false is returned.

Type and value equality matching is done as below:

- The types are compared for equality with their case ignored.

String values with different but equivalent usage of quoting,
escaping, or UTF8-hex-encoding are considered equal.
The case of the values is ignored during the comparison.

If obj is null or not an instance of Rdn, false is returned.

The types are compared for equality with their case ignored.

String values with different but equivalent usage of quoting,
escaping, or UTF8-hex-encoding are considered equal.
The case of the values is ignored during the comparison.

If obj is null or not an instance of Rdn, false is returned.

hashCode

```java
public int hashCode()
```

Returns the hash code of this RDN. Two RDNs that are
equal (according to the equals method) will have the same
hash code.

**Overrides:** hashCode

in class

Object
**Returns:** An int representing the hash code of this Rdn.
**See Also:** equals(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code of this RDN. Two RDNs that are
equal (according to the equals method) will have the same
hash code.

toAttributes

```java
public
Attributes
toAttributes()
```

Retrieves the

Attributes

view of the type/value mappings contained in this Rdn.

**Returns:** The non-null attributes containing the type/value
mappings of this Rdn.

---

#### toAttributes

public

Attributes

toAttributes()

Retrieves the

Attributes

view of the type/value mappings contained in this Rdn.

size

```java
public int size()
```

Retrieves the number of attribute type/value pairs in this Rdn.

**Returns:** The non-negative number of type/value pairs in this Rdn.

---

#### size

public int size()

Retrieves the number of attribute type/value pairs in this Rdn.

escapeValue

```java
public static
String
escapeValue​(
Object
val)
```

Given the value of an attribute, returns a string escaped according
to the rules specified in

RFC 2253

.

For example, if the val is "Sue, Grabbit and Runn", the escaped
value returned by this method is "Sue\, Grabbit and Runn".

A string value is represented as a String and binary value
as a byte array.

**Parameters:** val

- The non-null object to be escaped.
**Returns:** Escaped string value.
**Throws:** ClassCastException

- if val is not a String or byte array.

---

#### escapeValue

public static

String

escapeValue​(

Object

val)

Given the value of an attribute, returns a string escaped according
to the rules specified in

RFC 2253

.

For example, if the val is "Sue, Grabbit and Runn", the escaped
value returned by this method is "Sue\, Grabbit and Runn".

A string value is represented as a String and binary value
as a byte array.

For example, if the val is "Sue, Grabbit and Runn", the escaped
value returned by this method is "Sue\, Grabbit and Runn".

A string value is represented as a String and binary value
as a byte array.

A string value is represented as a String and binary value
as a byte array.

unescapeValue

```java
public static
Object
unescapeValue​(
String
val)
```

Given an attribute value string formatted according to the rules
specified in

RFC 2253

,
returns the unformatted value. Escapes and quotes are
stripped away, and hex-encoded UTF-8 is converted to equivalent
UTF-16 characters. Returns a string value as a String, and a
binary value as a byte array.

Legal and illegal values are defined in RFC 2253.
This method is generous in accepting the values and does not
catch all illegal values.
Therefore, passing in an illegal value might not necessarily
trigger an

IllegalArgumentException

.

**Parameters:** val

- The non-null string to be unescaped.
**Returns:** Unescaped value.
**Throws:** IllegalArgumentException

- When an Illegal value
is provided.

---

#### unescapeValue

public static

Object

unescapeValue​(

String

val)

Given an attribute value string formatted according to the rules
specified in

RFC 2253

,
returns the unformatted value. Escapes and quotes are
stripped away, and hex-encoded UTF-8 is converted to equivalent
UTF-16 characters. Returns a string value as a String, and a
binary value as a byte array.

Legal and illegal values are defined in RFC 2253.
This method is generous in accepting the values and does not
catch all illegal values.
Therefore, passing in an illegal value might not necessarily
trigger an

IllegalArgumentException

.

Legal and illegal values are defined in RFC 2253.
This method is generous in accepting the values and does not
catch all illegal values.
Therefore, passing in an illegal value might not necessarily
trigger an

IllegalArgumentException

.

---

