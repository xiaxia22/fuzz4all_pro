# Class KerberosCredMessage

**Source:** `java.security.jgss\javax\security\auth\kerberos\KerberosCredMessage.html`

### Class Description

```java
public final class
KerberosCredMessage

extends
Object

implements
Destroyable
```

This class encapsulates a Kerberos 5 KRB_CRED message which can be used to
send Kerberos credentials from one principal to another.

A KRB_CRED message is defined in Section 5.8.1 of the Kerberos Protocol
Specification (

RFC 4120

) as:

```java
KRB-CRED ::= [APPLICATION 22] SEQUENCE {
pvno [0] INTEGER (5),
msg-type [1] INTEGER (22),
tickets [2] SEQUENCE OF Ticket,
enc-part [3] EncryptedData -- EncKrbCredPart
}
```

**All Implemented Interfaces:** Destroyable

---

### Field Details

*No entries found.*

### Constructor Details

#### public KerberosCredMessage​(
KerberosPrincipal
sender,

KerberosPrincipal
recipient,
byte[] message)

Constructs a

KerberosCredMessage

object.

The contents of the

message

argument are copied; subsequent
modification of the byte array does not affect the newly created object.

**Parameters:**
- sender

- the sender of the message
- recipient

- the recipient of the message
- message

- the DER encoded KRB_CRED message

**Throws:**
- NullPointerException

- if any of sender, recipient
or message is null

---

### Method Details

#### public byte[] getEncoded()

Returns the DER encoded form of the KRB_CRED message.

**Returns:**
- a newly allocated byte array that contains the encoded form

**Throws:**
- IllegalStateException

- if the object is destroyed

---

#### public
KerberosPrincipal
getSender()

Returns the sender of this message.

**Returns:**
- the sender

**Throws:**
- IllegalStateException

- if the object is destroyed

---

#### public
KerberosPrincipal
getRecipient()

Returns the recipient of this message.

**Returns:**
- the recipient

**Throws:**
- IllegalStateException

- if the object is destroyed

---

#### public void destroy()

Destroys this object by clearing out the message.

**Specified by:**
- destroy

in interface

Destroyable

---

#### public
String
toString()

Returns an informative textual representation of this

KerberosCredMessage

.

**Overrides:**
- toString

in class

Object

**Returns:**
- an informative textual representation of this

KerberosCredMessage

.

---

#### public int hashCode()

Returns a hash code for this

KerberosCredMessage

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this

KerberosCredMessage

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
other)

Compares the specified object with this

KerberosCredMessage

for equality. Returns true if the given object is also a

KerberosCredMessage

and the two

KerberosCredMessage

instances are equivalent. More formally two

KerberosCredMessage

instances are equal if they have equal sender, recipient, and encoded
KRB_CRED messages.
A destroyed

KerberosCredMessage

object is only equal to itself.

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the object to compare to

**Returns:**
- true if the specified object is equal to this

KerberosCredMessage

, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class KerberosCredMessage

java.lang.Object

- javax.security.auth.kerberos.KerberosCredMessage

javax.security.auth.kerberos.KerberosCredMessage

**All Implemented Interfaces:** Destroyable

```java
public final class
KerberosCredMessage

extends
Object

implements
Destroyable
```

This class encapsulates a Kerberos 5 KRB_CRED message which can be used to
send Kerberos credentials from one principal to another.

A KRB_CRED message is defined in Section 5.8.1 of the Kerberos Protocol
Specification (

RFC 4120

) as:

```java
KRB-CRED ::= [APPLICATION 22] SEQUENCE {
pvno [0] INTEGER (5),
msg-type [1] INTEGER (22),
tickets [2] SEQUENCE OF Ticket,
enc-part [3] EncryptedData -- EncKrbCredPart
}
```

**Since:** 9

public final class

KerberosCredMessage

extends

Object

implements

Destroyable

This class encapsulates a Kerberos 5 KRB_CRED message which can be used to
send Kerberos credentials from one principal to another.

A KRB_CRED message is defined in Section 5.8.1 of the Kerberos Protocol
Specification (

RFC 4120

) as:

```java
KRB-CRED ::= [APPLICATION 22] SEQUENCE {
pvno [0] INTEGER (5),
msg-type [1] INTEGER (22),
tickets [2] SEQUENCE OF Ticket,
enc-part [3] EncryptedData -- EncKrbCredPart
}
```

A KRB_CRED message is defined in Section 5.8.1 of the Kerberos Protocol
Specification (

RFC 4120

) as:

```java
KRB-CRED ::= [APPLICATION 22] SEQUENCE {
pvno [0] INTEGER (5),
msg-type [1] INTEGER (22),
tickets [2] SEQUENCE OF Ticket,
enc-part [3] EncryptedData -- EncKrbCredPart
}
```

KRB-CRED ::= [APPLICATION 22] SEQUENCE {
pvno [0] INTEGER (5),
msg-type [1] INTEGER (22),
tickets [2] SEQUENCE OF Ticket,
enc-part [3] EncryptedData -- EncKrbCredPart
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KerberosCredMessage

​(

KerberosPrincipal

sender,

KerberosPrincipal

recipient,
byte[] message)

Constructs a

KerberosCredMessage

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

destroy

()

Destroys this object by clearing out the message.

boolean

equals

​(

Object

other)

Compares the specified object with this

KerberosCredMessage

for equality.

byte[]

getEncoded

()

Returns the DER encoded form of the KRB_CRED message.

KerberosPrincipal

getRecipient

()

Returns the recipient of this message.

KerberosPrincipal

getSender

()

Returns the sender of this message.

int

hashCode

()

Returns a hash code for this

KerberosCredMessage

.

String

toString

()

Returns an informative textual representation of this

KerberosCredMessage

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

- Methods declared in interface javax.security.auth.

Destroyable

isDestroyed

Constructor Summary

Constructors

Constructor

Description

KerberosCredMessage

​(

KerberosPrincipal

sender,

KerberosPrincipal

recipient,
byte[] message)

Constructs a

KerberosCredMessage

object.

---

#### Constructor Summary

Constructs a

KerberosCredMessage

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

destroy

()

Destroys this object by clearing out the message.

boolean

equals

​(

Object

other)

Compares the specified object with this

KerberosCredMessage

for equality.

byte[]

getEncoded

()

Returns the DER encoded form of the KRB_CRED message.

KerberosPrincipal

getRecipient

()

Returns the recipient of this message.

KerberosPrincipal

getSender

()

Returns the sender of this message.

int

hashCode

()

Returns a hash code for this

KerberosCredMessage

.

String

toString

()

Returns an informative textual representation of this

KerberosCredMessage

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

- Methods declared in interface javax.security.auth.

Destroyable

isDestroyed

---

#### Method Summary

Destroys this object by clearing out the message.

Compares the specified object with this

KerberosCredMessage

for equality.

Returns the DER encoded form of the KRB_CRED message.

Returns the recipient of this message.

Returns the sender of this message.

Returns a hash code for this

KerberosCredMessage

.

Returns an informative textual representation of this

KerberosCredMessage

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

Methods declared in interface javax.security.auth.

Destroyable

isDestroyed

---

#### Methods declared in interface javax.security.auth. Destroyable

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- KerberosCredMessage

```java
public KerberosCredMessage​(
KerberosPrincipal
sender,

KerberosPrincipal
recipient,
byte[] message)
```

Constructs a

KerberosCredMessage

object.

The contents of the

message

argument are copied; subsequent
modification of the byte array does not affect the newly created object.

**Parameters:** sender

- the sender of the message
**Parameters:** recipient

- the recipient of the message
**Parameters:** message

- the DER encoded KRB_CRED message
**Throws:** NullPointerException

- if any of sender, recipient
or message is null

============ METHOD DETAIL ==========

- Method Detail

- getEncoded

```java
public byte[] getEncoded()
```

Returns the DER encoded form of the KRB_CRED message.

**Returns:** a newly allocated byte array that contains the encoded form
**Throws:** IllegalStateException

- if the object is destroyed

- getSender

```java
public
KerberosPrincipal
getSender()
```

Returns the sender of this message.

**Returns:** the sender
**Throws:** IllegalStateException

- if the object is destroyed

- getRecipient

```java
public
KerberosPrincipal
getRecipient()
```

Returns the recipient of this message.

**Returns:** the recipient
**Throws:** IllegalStateException

- if the object is destroyed

- destroy

```java
public void destroy()
```

Destroys this object by clearing out the message.

**Specified by:** destroy

in interface

Destroyable

- toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosCredMessage

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosCredMessage

.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosCredMessage

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosCredMessage

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

Compares the specified object with this

KerberosCredMessage

for equality. Returns true if the given object is also a

KerberosCredMessage

and the two

KerberosCredMessage

instances are equivalent. More formally two

KerberosCredMessage

instances are equal if they have equal sender, recipient, and encoded
KRB_CRED messages.
A destroyed

KerberosCredMessage

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

KerberosCredMessage

, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- KerberosCredMessage

```java
public KerberosCredMessage​(
KerberosPrincipal
sender,

KerberosPrincipal
recipient,
byte[] message)
```

Constructs a

KerberosCredMessage

object.

The contents of the

message

argument are copied; subsequent
modification of the byte array does not affect the newly created object.

**Parameters:** sender

- the sender of the message
**Parameters:** recipient

- the recipient of the message
**Parameters:** message

- the DER encoded KRB_CRED message
**Throws:** NullPointerException

- if any of sender, recipient
or message is null

---

#### Constructor Detail

KerberosCredMessage

```java
public KerberosCredMessage​(
KerberosPrincipal
sender,

KerberosPrincipal
recipient,
byte[] message)
```

Constructs a

KerberosCredMessage

object.

The contents of the

message

argument are copied; subsequent
modification of the byte array does not affect the newly created object.

**Parameters:** sender

- the sender of the message
**Parameters:** recipient

- the recipient of the message
**Parameters:** message

- the DER encoded KRB_CRED message
**Throws:** NullPointerException

- if any of sender, recipient
or message is null

---

#### KerberosCredMessage

public KerberosCredMessage​(

KerberosPrincipal

sender,

KerberosPrincipal

recipient,
byte[] message)

Constructs a

KerberosCredMessage

object.

The contents of the

message

argument are copied; subsequent
modification of the byte array does not affect the newly created object.

The contents of the

message

argument are copied; subsequent
modification of the byte array does not affect the newly created object.

Method Detail

- getEncoded

```java
public byte[] getEncoded()
```

Returns the DER encoded form of the KRB_CRED message.

**Returns:** a newly allocated byte array that contains the encoded form
**Throws:** IllegalStateException

- if the object is destroyed

- getSender

```java
public
KerberosPrincipal
getSender()
```

Returns the sender of this message.

**Returns:** the sender
**Throws:** IllegalStateException

- if the object is destroyed

- getRecipient

```java
public
KerberosPrincipal
getRecipient()
```

Returns the recipient of this message.

**Returns:** the recipient
**Throws:** IllegalStateException

- if the object is destroyed

- destroy

```java
public void destroy()
```

Destroys this object by clearing out the message.

**Specified by:** destroy

in interface

Destroyable

- toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosCredMessage

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosCredMessage

.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosCredMessage

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosCredMessage

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

Compares the specified object with this

KerberosCredMessage

for equality. Returns true if the given object is also a

KerberosCredMessage

and the two

KerberosCredMessage

instances are equivalent. More formally two

KerberosCredMessage

instances are equal if they have equal sender, recipient, and encoded
KRB_CRED messages.
A destroyed

KerberosCredMessage

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

KerberosCredMessage

, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

getEncoded

```java
public byte[] getEncoded()
```

Returns the DER encoded form of the KRB_CRED message.

**Returns:** a newly allocated byte array that contains the encoded form
**Throws:** IllegalStateException

- if the object is destroyed

---

#### getEncoded

public byte[] getEncoded()

Returns the DER encoded form of the KRB_CRED message.

getSender

```java
public
KerberosPrincipal
getSender()
```

Returns the sender of this message.

**Returns:** the sender
**Throws:** IllegalStateException

- if the object is destroyed

---

#### getSender

public

KerberosPrincipal

getSender()

Returns the sender of this message.

getRecipient

```java
public
KerberosPrincipal
getRecipient()
```

Returns the recipient of this message.

**Returns:** the recipient
**Throws:** IllegalStateException

- if the object is destroyed

---

#### getRecipient

public

KerberosPrincipal

getRecipient()

Returns the recipient of this message.

destroy

```java
public void destroy()
```

Destroys this object by clearing out the message.

**Specified by:** destroy

in interface

Destroyable

---

#### destroy

public void destroy()

Destroys this object by clearing out the message.

toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosCredMessage

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosCredMessage

.

---

#### toString

public

String

toString()

Returns an informative textual representation of this

KerberosCredMessage

.

hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosCredMessage

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosCredMessage

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this

KerberosCredMessage

.

equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this

KerberosCredMessage

for equality. Returns true if the given object is also a

KerberosCredMessage

and the two

KerberosCredMessage

instances are equivalent. More formally two

KerberosCredMessage

instances are equal if they have equal sender, recipient, and encoded
KRB_CRED messages.
A destroyed

KerberosCredMessage

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

KerberosCredMessage

, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Compares the specified object with this

KerberosCredMessage

for equality. Returns true if the given object is also a

KerberosCredMessage

and the two

KerberosCredMessage

instances are equivalent. More formally two

KerberosCredMessage

instances are equal if they have equal sender, recipient, and encoded
KRB_CRED messages.
A destroyed

KerberosCredMessage

object is only equal to itself.

---

