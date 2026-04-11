# Class KerberosPrincipal

**Source:** `java.security.jgss\javax\security\auth\kerberos\KerberosPrincipal.html`

### Class Description

```java
public final class
KerberosPrincipal

extends
Object

implements
Principal
,
Serializable
```

This class encapsulates a Kerberos principal.

**All Implemented Interfaces:** Serializable

,

Principal

---

### Field Details

#### public static final int KRB_NT_UNKNOWN

unknown name type.

**See Also:**
- Constant Field Values

---

#### public static final int KRB_NT_PRINCIPAL

user principal name type.

**See Also:**
- Constant Field Values

---

#### public static final int KRB_NT_SRV_INST

service and other unique instance (krbtgt) name type.

**See Also:**
- Constant Field Values

---

#### public static final int KRB_NT_SRV_HST

service with host name as instance (telnet, rcommands) name type.

**See Also:**
- Constant Field Values

---

#### public static final int KRB_NT_SRV_XHST

service with host as remaining components name type.

**See Also:**
- Constant Field Values

---

#### public static final int KRB_NT_UID

unique ID name type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public KerberosPrincipal​(
String
name)

Constructs a

KerberosPrincipal

from the provided string input.
The name type for this principal defaults to

KRB_NT_PRINCIPAL

This string is assumed to contain a name in the format
that is specified in Section 2.1.1. (Kerberos Principal Name Form) of

RFC 1964

(for example,

duke@FOO.COM

, where

duke

represents a principal, and

FOO.COM

represents a realm).

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

**Parameters:**
- name

- the principal name

**Throws:**
- IllegalArgumentException

- if name is improperly
formatted, if name is null, or if name does not contain
the realm to use and the default realm is not specified
in either a Kerberos configuration file or via the
java.security.krb5.realm system property.
- SecurityException

- if a security manager is installed and

name

does not contain the realm to use, and a proper

ServicePermission

as described above is not granted.

---

#### public KerberosPrincipal​(
String
name,
int nameType)

Constructs a

KerberosPrincipal

from the provided string and
name type input. The string is assumed to contain a name in the
format that is specified in Section 2.1 (Mandatory Name Forms) of

RFC 1964

.
Valid name types are specified in Section 6.2 (Principal Names) of

RFC 4120

.
The input name must be consistent with the provided name type.
(for example,

duke@FOO.COM

, is a valid input string for the
name type, KRB_NT_PRINCIPAL where

duke

represents a principal, and

FOO.COM

represents a realm).

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

**Parameters:**
- name

- the principal name
- nameType

- the name type of the principal

**Throws:**
- IllegalArgumentException

- if name is improperly
formatted, if name is null, if the nameType is not supported,
or if name does not contain the realm to use and the default
realm is not specified in either a Kerberos configuration
file or via the java.security.krb5.realm system property.
- SecurityException

- if a security manager is installed and

name

does not contain the realm to use, and a proper

ServicePermission

as described above is not granted.

---

### Method Details

#### public
String
getRealm()

Returns the realm component of this Kerberos principal.

**Returns:**
- the realm component of this Kerberos principal.

---

#### public int hashCode()

Returns a hash code for this

KerberosPrincipal

. The hash code
is defined to be the result of the following calculation:

```java
hashCode = getName().hashCode();
```

**Specified by:**
- hashCode

in interface

Principal

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this

KerberosPrincipal

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
other)

Compares the specified object with this principal for equality.
Returns true if the given object is also a

KerberosPrincipal

and the two

KerberosPrincipal

instances are equivalent.
More formally two

KerberosPrincipal

instances are equal
if the values returned by

getName()

are equal.

**Specified by:**
- equals

in interface

Principal

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the object to compare to

**Returns:**
- true if the object passed in represents the same principal
as this one, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
getName()

The returned string corresponds to the single-string
representation of a Kerberos Principal name as specified in
Section 2.1 of

RFC 1964

.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- the principal name.

---

#### public int getNameType()

Returns the name type of the

KerberosPrincipal

. Valid name types
are specified in Section 6.2 of

RFC4120

.

**Returns:**
- the name type.

---

#### public
String
toString()

Returns an informative textual representation of this

KerberosPrincipal

.

**Specified by:**
- toString

in interface

Principal

**Overrides:**
- toString

in class

Object

**Returns:**
- an informative textual representation of this

KerberosPrincipal

.

---

### Additional Sections

#### Class KerberosPrincipal

java.lang.Object

- javax.security.auth.kerberos.KerberosPrincipal

javax.security.auth.kerberos.KerberosPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public final class
KerberosPrincipal

extends
Object

implements
Principal
,
Serializable
```

This class encapsulates a Kerberos principal.

**Since:** 1.4
**See Also:** Serialized Form

public final class

KerberosPrincipal

extends

Object

implements

Principal

,

Serializable

This class encapsulates a Kerberos principal.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

KRB_NT_PRINCIPAL

user principal name type.

static int

KRB_NT_SRV_HST

service with host name as instance (telnet, rcommands) name type.

static int

KRB_NT_SRV_INST

service and other unique instance (krbtgt) name type.

static int

KRB_NT_SRV_XHST

service with host as remaining components name type.

static int

KRB_NT_UID

unique ID name type.

static int

KRB_NT_UNKNOWN

unknown name type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KerberosPrincipal

​(

String

name)

Constructs a

KerberosPrincipal

from the provided string input.

KerberosPrincipal

​(

String

name,
int nameType)

Constructs a

KerberosPrincipal

from the provided string and
name type input.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Compares the specified object with this principal for equality.

String

getName

()

The returned string corresponds to the single-string
representation of a Kerberos Principal name as specified in
Section 2.1 of

RFC 1964

.

int

getNameType

()

Returns the name type of the

KerberosPrincipal

.

String

getRealm

()

Returns the realm component of this Kerberos principal.

int

hashCode

()

Returns a hash code for this

KerberosPrincipal

.

String

toString

()

Returns an informative textual representation of this

KerberosPrincipal

.

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

- Methods declared in interface java.security.

Principal

implies

Field Summary

Fields

Modifier and Type

Field

Description

static int

KRB_NT_PRINCIPAL

user principal name type.

static int

KRB_NT_SRV_HST

service with host name as instance (telnet, rcommands) name type.

static int

KRB_NT_SRV_INST

service and other unique instance (krbtgt) name type.

static int

KRB_NT_SRV_XHST

service with host as remaining components name type.

static int

KRB_NT_UID

unique ID name type.

static int

KRB_NT_UNKNOWN

unknown name type.

---

#### Field Summary

user principal name type.

service with host name as instance (telnet, rcommands) name type.

service and other unique instance (krbtgt) name type.

service with host as remaining components name type.

unique ID name type.

unknown name type.

Constructor Summary

Constructors

Constructor

Description

KerberosPrincipal

​(

String

name)

Constructs a

KerberosPrincipal

from the provided string input.

KerberosPrincipal

​(

String

name,
int nameType)

Constructs a

KerberosPrincipal

from the provided string and
name type input.

---

#### Constructor Summary

Constructs a

KerberosPrincipal

from the provided string input.

Constructs a

KerberosPrincipal

from the provided string and
name type input.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Compares the specified object with this principal for equality.

String

getName

()

The returned string corresponds to the single-string
representation of a Kerberos Principal name as specified in
Section 2.1 of

RFC 1964

.

int

getNameType

()

Returns the name type of the

KerberosPrincipal

.

String

getRealm

()

Returns the realm component of this Kerberos principal.

int

hashCode

()

Returns a hash code for this

KerberosPrincipal

.

String

toString

()

Returns an informative textual representation of this

KerberosPrincipal

.

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

- Methods declared in interface java.security.

Principal

implies

---

#### Method Summary

Compares the specified object with this principal for equality.

The returned string corresponds to the single-string
representation of a Kerberos Principal name as specified in
Section 2.1 of

RFC 1964

.

Returns the name type of the

KerberosPrincipal

.

Returns the realm component of this Kerberos principal.

Returns a hash code for this

KerberosPrincipal

.

Returns an informative textual representation of this

KerberosPrincipal

.

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

Methods declared in interface java.security.

Principal

implies

---

#### Methods declared in interface java.security. Principal

============ FIELD DETAIL ===========

- Field Detail

- KRB_NT_UNKNOWN

```java
public static final int KRB_NT_UNKNOWN
```

unknown name type.

**See Also:** Constant Field Values

- KRB_NT_PRINCIPAL

```java
public static final int KRB_NT_PRINCIPAL
```

user principal name type.

**See Also:** Constant Field Values

- KRB_NT_SRV_INST

```java
public static final int KRB_NT_SRV_INST
```

service and other unique instance (krbtgt) name type.

**See Also:** Constant Field Values

- KRB_NT_SRV_HST

```java
public static final int KRB_NT_SRV_HST
```

service with host name as instance (telnet, rcommands) name type.

**See Also:** Constant Field Values

- KRB_NT_SRV_XHST

```java
public static final int KRB_NT_SRV_XHST
```

service with host as remaining components name type.

**See Also:** Constant Field Values

- KRB_NT_UID

```java
public static final int KRB_NT_UID
```

unique ID name type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- KerberosPrincipal

```java
public KerberosPrincipal​(
String
name)
```

Constructs a

KerberosPrincipal

from the provided string input.
The name type for this principal defaults to

KRB_NT_PRINCIPAL

This string is assumed to contain a name in the format
that is specified in Section 2.1.1. (Kerberos Principal Name Form) of

RFC 1964

(for example,

duke@FOO.COM

, where

duke

represents a principal, and

FOO.COM

represents a realm).

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

**Parameters:** name

- the principal name
**Throws:** IllegalArgumentException

- if name is improperly
formatted, if name is null, or if name does not contain
the realm to use and the default realm is not specified
in either a Kerberos configuration file or via the
java.security.krb5.realm system property.
**Throws:** SecurityException

- if a security manager is installed and

name

does not contain the realm to use, and a proper

ServicePermission

as described above is not granted.

- KerberosPrincipal

```java
public KerberosPrincipal​(
String
name,
int nameType)
```

Constructs a

KerberosPrincipal

from the provided string and
name type input. The string is assumed to contain a name in the
format that is specified in Section 2.1 (Mandatory Name Forms) of

RFC 1964

.
Valid name types are specified in Section 6.2 (Principal Names) of

RFC 4120

.
The input name must be consistent with the provided name type.
(for example,

duke@FOO.COM

, is a valid input string for the
name type, KRB_NT_PRINCIPAL where

duke

represents a principal, and

FOO.COM

represents a realm).

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

**Parameters:** name

- the principal name
**Parameters:** nameType

- the name type of the principal
**Throws:** IllegalArgumentException

- if name is improperly
formatted, if name is null, if the nameType is not supported,
or if name does not contain the realm to use and the default
realm is not specified in either a Kerberos configuration
file or via the java.security.krb5.realm system property.
**Throws:** SecurityException

- if a security manager is installed and

name

does not contain the realm to use, and a proper

ServicePermission

as described above is not granted.

============ METHOD DETAIL ==========

- Method Detail

- getRealm

```java
public
String
getRealm()
```

Returns the realm component of this Kerberos principal.

**Returns:** the realm component of this Kerberos principal.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosPrincipal

. The hash code
is defined to be the result of the following calculation:

```java
hashCode = getName().hashCode();
```

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this principal for equality.
Returns true if the given object is also a

KerberosPrincipal

and the two

KerberosPrincipal

instances are equivalent.
More formally two

KerberosPrincipal

instances are equal
if the values returned by

getName()

are equal.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the object passed in represents the same principal
as this one, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- getName

```java
public
String
getName()
```

The returned string corresponds to the single-string
representation of a Kerberos Principal name as specified in
Section 2.1 of

RFC 1964

.

**Specified by:** getName

in interface

Principal
**Returns:** the principal name.

- getNameType

```java
public int getNameType()
```

Returns the name type of the

KerberosPrincipal

. Valid name types
are specified in Section 6.2 of

RFC4120

.

**Returns:** the name type.

- toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosPrincipal

.

Field Detail

- KRB_NT_UNKNOWN

```java
public static final int KRB_NT_UNKNOWN
```

unknown name type.

**See Also:** Constant Field Values

- KRB_NT_PRINCIPAL

```java
public static final int KRB_NT_PRINCIPAL
```

user principal name type.

**See Also:** Constant Field Values

- KRB_NT_SRV_INST

```java
public static final int KRB_NT_SRV_INST
```

service and other unique instance (krbtgt) name type.

**See Also:** Constant Field Values

- KRB_NT_SRV_HST

```java
public static final int KRB_NT_SRV_HST
```

service with host name as instance (telnet, rcommands) name type.

**See Also:** Constant Field Values

- KRB_NT_SRV_XHST

```java
public static final int KRB_NT_SRV_XHST
```

service with host as remaining components name type.

**See Also:** Constant Field Values

- KRB_NT_UID

```java
public static final int KRB_NT_UID
```

unique ID name type.

**See Also:** Constant Field Values

---

#### Field Detail

KRB_NT_UNKNOWN

```java
public static final int KRB_NT_UNKNOWN
```

unknown name type.

**See Also:** Constant Field Values

---

#### KRB_NT_UNKNOWN

public static final int KRB_NT_UNKNOWN

unknown name type.

KRB_NT_PRINCIPAL

```java
public static final int KRB_NT_PRINCIPAL
```

user principal name type.

**See Also:** Constant Field Values

---

#### KRB_NT_PRINCIPAL

public static final int KRB_NT_PRINCIPAL

user principal name type.

KRB_NT_SRV_INST

```java
public static final int KRB_NT_SRV_INST
```

service and other unique instance (krbtgt) name type.

**See Also:** Constant Field Values

---

#### KRB_NT_SRV_INST

public static final int KRB_NT_SRV_INST

service and other unique instance (krbtgt) name type.

KRB_NT_SRV_HST

```java
public static final int KRB_NT_SRV_HST
```

service with host name as instance (telnet, rcommands) name type.

**See Also:** Constant Field Values

---

#### KRB_NT_SRV_HST

public static final int KRB_NT_SRV_HST

service with host name as instance (telnet, rcommands) name type.

KRB_NT_SRV_XHST

```java
public static final int KRB_NT_SRV_XHST
```

service with host as remaining components name type.

**See Also:** Constant Field Values

---

#### KRB_NT_SRV_XHST

public static final int KRB_NT_SRV_XHST

service with host as remaining components name type.

KRB_NT_UID

```java
public static final int KRB_NT_UID
```

unique ID name type.

**See Also:** Constant Field Values

---

#### KRB_NT_UID

public static final int KRB_NT_UID

unique ID name type.

Constructor Detail

- KerberosPrincipal

```java
public KerberosPrincipal​(
String
name)
```

Constructs a

KerberosPrincipal

from the provided string input.
The name type for this principal defaults to

KRB_NT_PRINCIPAL

This string is assumed to contain a name in the format
that is specified in Section 2.1.1. (Kerberos Principal Name Form) of

RFC 1964

(for example,

duke@FOO.COM

, where

duke

represents a principal, and

FOO.COM

represents a realm).

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

**Parameters:** name

- the principal name
**Throws:** IllegalArgumentException

- if name is improperly
formatted, if name is null, or if name does not contain
the realm to use and the default realm is not specified
in either a Kerberos configuration file or via the
java.security.krb5.realm system property.
**Throws:** SecurityException

- if a security manager is installed and

name

does not contain the realm to use, and a proper

ServicePermission

as described above is not granted.

- KerberosPrincipal

```java
public KerberosPrincipal​(
String
name,
int nameType)
```

Constructs a

KerberosPrincipal

from the provided string and
name type input. The string is assumed to contain a name in the
format that is specified in Section 2.1 (Mandatory Name Forms) of

RFC 1964

.
Valid name types are specified in Section 6.2 (Principal Names) of

RFC 4120

.
The input name must be consistent with the provided name type.
(for example,

duke@FOO.COM

, is a valid input string for the
name type, KRB_NT_PRINCIPAL where

duke

represents a principal, and

FOO.COM

represents a realm).

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

**Parameters:** name

- the principal name
**Parameters:** nameType

- the name type of the principal
**Throws:** IllegalArgumentException

- if name is improperly
formatted, if name is null, if the nameType is not supported,
or if name does not contain the realm to use and the default
realm is not specified in either a Kerberos configuration
file or via the java.security.krb5.realm system property.
**Throws:** SecurityException

- if a security manager is installed and

name

does not contain the realm to use, and a proper

ServicePermission

as described above is not granted.

---

#### Constructor Detail

KerberosPrincipal

```java
public KerberosPrincipal​(
String
name)
```

Constructs a

KerberosPrincipal

from the provided string input.
The name type for this principal defaults to

KRB_NT_PRINCIPAL

This string is assumed to contain a name in the format
that is specified in Section 2.1.1. (Kerberos Principal Name Form) of

RFC 1964

(for example,

duke@FOO.COM

, where

duke

represents a principal, and

FOO.COM

represents a realm).

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

**Parameters:** name

- the principal name
**Throws:** IllegalArgumentException

- if name is improperly
formatted, if name is null, or if name does not contain
the realm to use and the default realm is not specified
in either a Kerberos configuration file or via the
java.security.krb5.realm system property.
**Throws:** SecurityException

- if a security manager is installed and

name

does not contain the realm to use, and a proper

ServicePermission

as described above is not granted.

---

#### KerberosPrincipal

public KerberosPrincipal​(

String

name)

Constructs a

KerberosPrincipal

from the provided string input.
The name type for this principal defaults to

KRB_NT_PRINCIPAL

This string is assumed to contain a name in the format
that is specified in Section 2.1.1. (Kerberos Principal Name Form) of

RFC 1964

(for example,

duke@FOO.COM

, where

duke

represents a principal, and

FOO.COM

represents a realm).

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

KerberosPrincipal

```java
public KerberosPrincipal​(
String
name,
int nameType)
```

Constructs a

KerberosPrincipal

from the provided string and
name type input. The string is assumed to contain a name in the
format that is specified in Section 2.1 (Mandatory Name Forms) of

RFC 1964

.
Valid name types are specified in Section 6.2 (Principal Names) of

RFC 4120

.
The input name must be consistent with the provided name type.
(for example,

duke@FOO.COM

, is a valid input string for the
name type, KRB_NT_PRINCIPAL where

duke

represents a principal, and

FOO.COM

represents a realm).

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

**Parameters:** name

- the principal name
**Parameters:** nameType

- the name type of the principal
**Throws:** IllegalArgumentException

- if name is improperly
formatted, if name is null, if the nameType is not supported,
or if name does not contain the realm to use and the default
realm is not specified in either a Kerberos configuration
file or via the java.security.krb5.realm system property.
**Throws:** SecurityException

- if a security manager is installed and

name

does not contain the realm to use, and a proper

ServicePermission

as described above is not granted.

---

#### KerberosPrincipal

public KerberosPrincipal​(

String

name,
int nameType)

Constructs a

KerberosPrincipal

from the provided string and
name type input. The string is assumed to contain a name in the
format that is specified in Section 2.1 (Mandatory Name Forms) of

RFC 1964

.
Valid name types are specified in Section 6.2 (Principal Names) of

RFC 4120

.
The input name must be consistent with the provided name type.
(for example,

duke@FOO.COM

, is a valid input string for the
name type, KRB_NT_PRINCIPAL where

duke

represents a principal, and

FOO.COM

represents a realm).

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

If the input name does not contain a realm, the default realm
is used. The default realm can be specified either in a Kerberos
configuration file or via the java.security.krb5.realm
system property. For more information, see the

Kerberos Requirements

.
Additionally, if a security manager is
installed, a

ServicePermission

must be granted and the service
principal of the permission must minimally be inside the

KerberosPrincipal

's realm. For example, if the result of

new KerberosPrincipal("user")

is

user@EXAMPLE.COM

,
then a

ServicePermission

with service principal

host/www.example.com@EXAMPLE.COM

(and any action)
must be granted.

Method Detail

- getRealm

```java
public
String
getRealm()
```

Returns the realm component of this Kerberos principal.

**Returns:** the realm component of this Kerberos principal.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosPrincipal

. The hash code
is defined to be the result of the following calculation:

```java
hashCode = getName().hashCode();
```

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this principal for equality.
Returns true if the given object is also a

KerberosPrincipal

and the two

KerberosPrincipal

instances are equivalent.
More formally two

KerberosPrincipal

instances are equal
if the values returned by

getName()

are equal.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the object passed in represents the same principal
as this one, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- getName

```java
public
String
getName()
```

The returned string corresponds to the single-string
representation of a Kerberos Principal name as specified in
Section 2.1 of

RFC 1964

.

**Specified by:** getName

in interface

Principal
**Returns:** the principal name.

- getNameType

```java
public int getNameType()
```

Returns the name type of the

KerberosPrincipal

. Valid name types
are specified in Section 6.2 of

RFC4120

.

**Returns:** the name type.

- toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosPrincipal

.

---

#### Method Detail

getRealm

```java
public
String
getRealm()
```

Returns the realm component of this Kerberos principal.

**Returns:** the realm component of this Kerberos principal.

---

#### getRealm

public

String

getRealm()

Returns the realm component of this Kerberos principal.

hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosPrincipal

. The hash code
is defined to be the result of the following calculation:

```java
hashCode = getName().hashCode();
```

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this

KerberosPrincipal

. The hash code
is defined to be the result of the following calculation:

```java
hashCode = getName().hashCode();
```

hashCode = getName().hashCode();

equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this principal for equality.
Returns true if the given object is also a

KerberosPrincipal

and the two

KerberosPrincipal

instances are equivalent.
More formally two

KerberosPrincipal

instances are equal
if the values returned by

getName()

are equal.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the object passed in represents the same principal
as this one, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Compares the specified object with this principal for equality.
Returns true if the given object is also a

KerberosPrincipal

and the two

KerberosPrincipal

instances are equivalent.
More formally two

KerberosPrincipal

instances are equal
if the values returned by

getName()

are equal.

getName

```java
public
String
getName()
```

The returned string corresponds to the single-string
representation of a Kerberos Principal name as specified in
Section 2.1 of

RFC 1964

.

**Specified by:** getName

in interface

Principal
**Returns:** the principal name.

---

#### getName

public

String

getName()

The returned string corresponds to the single-string
representation of a Kerberos Principal name as specified in
Section 2.1 of

RFC 1964

.

getNameType

```java
public int getNameType()
```

Returns the name type of the

KerberosPrincipal

. Valid name types
are specified in Section 6.2 of

RFC4120

.

**Returns:** the name type.

---

#### getNameType

public int getNameType()

Returns the name type of the

KerberosPrincipal

. Valid name types
are specified in Section 6.2 of

RFC4120

.

toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosPrincipal

.

---

#### toString

public

String

toString()

Returns an informative textual representation of this

KerberosPrincipal

.

---

