# Class ChannelBinding

**Source:** `java.security.jgss\org\ietf\jgss\ChannelBinding.html`

### Class Description

```java
public class
ChannelBinding

extends
Object
```

This class encapsulates the concept of caller-provided channel
binding information. Channel bindings are used to strengthen the
quality with which peer entity authentication is provided during
context establishment. They enable the GSS-API callers to bind the
establishment of the security context to relevant characteristics
like addresses or to application specific data.

The caller initiating the security context must determine the
appropriate channel binding values to set in the GSSContext object.
The acceptor must provide an identical binding in order to validate
that received tokens possess correct channel-related characteristics.

Use of channel bindings is optional in GSS-API. ChannelBinding can be
set for the

GSSContext

using the

setChannelBinding

method
before the first call to

initSecContext

or

acceptSecContext

has been performed. Unless the

setChannelBinding

method has been used to set the ChannelBinding for a GSSContext object,

null

ChannelBinding will be assumed.

Conceptually, the GSS-API concatenates the initiator and acceptor
address information, and the application supplied byte array to form an
octet string. The mechanism calculates a MIC over this octet string and
binds the MIC to the context establishment token emitted by

initSecContext

method of the

GSSContext

interface. The same bindings are set by the context acceptor for its

GSSContext

object and during processing of the

acceptSecContext

method a MIC is calculated in the same
way. The calculated MIC is compared with that found in the token, and if
the MICs differ, accept will throw a

GSSException

with the
major code set to

BAD_BINDINGS

, and
the context will not be established. Some mechanisms may include the
actual channel binding data in the token (rather than just a MIC);
applications should therefore not use confidential data as
channel-binding components.

Individual mechanisms may impose additional constraints on addresses
that may appear in channel bindings. For example, a mechanism may
verify that the initiator address field of the channel binding
contains the correct network address of the host system. Portable
applications should therefore ensure that they either provide correct
information for the address fields, or omit setting of the addressing
information.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### public ChannelBinding​(
InetAddress
initAddr,

InetAddress
acceptAddr,
byte[] appData)

Create a ChannelBinding object with user supplied address information
and data.

null

values can be used for any fields which the
application does not want to specify.

**Parameters:**
- initAddr

- the address of the context initiator.

null

value can be supplied to indicate that the
application does not want to set this value.
- acceptAddr

- the address of the context
acceptor.

null

value can be supplied to indicate that
the application does not want to set this value.
- appData

- application supplied data to be used as part of the
channel bindings.

null

value can be supplied to
indicate that the application does not want to set this value.

---

#### public ChannelBinding​(byte[] appData)

Creates a ChannelBinding object without any addressing information.

**Parameters:**
- appData

- application supplied data to be used as part of the
channel bindings.

---

### Method Details

#### public
InetAddress
getInitiatorAddress()

Get the initiator's address for this channel binding.

**Returns:**
- the initiator's address.

null

is returned if
the address has not been set.

---

#### public
InetAddress
getAcceptorAddress()

Get the acceptor's address for this channel binding.

**Returns:**
- the acceptor's address. null is returned if the address has
not been set.

---

#### public byte[] getApplicationData()

Get the application specified data for this channel binding.

**Returns:**
- the application data being used as part of the
ChannelBinding.

null

is returned if no application data
has been specified for the channel binding.

---

#### public boolean equals​(
Object
obj)

Compares two instances of ChannelBinding.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- another ChannelBinding to compare this one with

**Returns:**
- true if the two ChannelBinding's contain
the same values for the initiator and acceptor addresses and the
application data.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hashcode value for this ChannelBinding object.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hashCode value

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class ChannelBinding

java.lang.Object

- org.ietf.jgss.ChannelBinding

org.ietf.jgss.ChannelBinding

```java
public class
ChannelBinding

extends
Object
```

This class encapsulates the concept of caller-provided channel
binding information. Channel bindings are used to strengthen the
quality with which peer entity authentication is provided during
context establishment. They enable the GSS-API callers to bind the
establishment of the security context to relevant characteristics
like addresses or to application specific data.

The caller initiating the security context must determine the
appropriate channel binding values to set in the GSSContext object.
The acceptor must provide an identical binding in order to validate
that received tokens possess correct channel-related characteristics.

Use of channel bindings is optional in GSS-API. ChannelBinding can be
set for the

GSSContext

using the

setChannelBinding

method
before the first call to

initSecContext

or

acceptSecContext

has been performed. Unless the

setChannelBinding

method has been used to set the ChannelBinding for a GSSContext object,

null

ChannelBinding will be assumed.

Conceptually, the GSS-API concatenates the initiator and acceptor
address information, and the application supplied byte array to form an
octet string. The mechanism calculates a MIC over this octet string and
binds the MIC to the context establishment token emitted by

initSecContext

method of the

GSSContext

interface. The same bindings are set by the context acceptor for its

GSSContext

object and during processing of the

acceptSecContext

method a MIC is calculated in the same
way. The calculated MIC is compared with that found in the token, and if
the MICs differ, accept will throw a

GSSException

with the
major code set to

BAD_BINDINGS

, and
the context will not be established. Some mechanisms may include the
actual channel binding data in the token (rather than just a MIC);
applications should therefore not use confidential data as
channel-binding components.

Individual mechanisms may impose additional constraints on addresses
that may appear in channel bindings. For example, a mechanism may
verify that the initiator address field of the channel binding
contains the correct network address of the host system. Portable
applications should therefore ensure that they either provide correct
information for the address fields, or omit setting of the addressing
information.

**Since:** 1.4

public class

ChannelBinding

extends

Object

This class encapsulates the concept of caller-provided channel
binding information. Channel bindings are used to strengthen the
quality with which peer entity authentication is provided during
context establishment. They enable the GSS-API callers to bind the
establishment of the security context to relevant characteristics
like addresses or to application specific data.

The caller initiating the security context must determine the
appropriate channel binding values to set in the GSSContext object.
The acceptor must provide an identical binding in order to validate
that received tokens possess correct channel-related characteristics.

Use of channel bindings is optional in GSS-API. ChannelBinding can be
set for the

GSSContext

using the

setChannelBinding

method
before the first call to

initSecContext

or

acceptSecContext

has been performed. Unless the

setChannelBinding

method has been used to set the ChannelBinding for a GSSContext object,

null

ChannelBinding will be assumed.

Conceptually, the GSS-API concatenates the initiator and acceptor
address information, and the application supplied byte array to form an
octet string. The mechanism calculates a MIC over this octet string and
binds the MIC to the context establishment token emitted by

initSecContext

method of the

GSSContext

interface. The same bindings are set by the context acceptor for its

GSSContext

object and during processing of the

acceptSecContext

method a MIC is calculated in the same
way. The calculated MIC is compared with that found in the token, and if
the MICs differ, accept will throw a

GSSException

with the
major code set to

BAD_BINDINGS

, and
the context will not be established. Some mechanisms may include the
actual channel binding data in the token (rather than just a MIC);
applications should therefore not use confidential data as
channel-binding components.

Individual mechanisms may impose additional constraints on addresses
that may appear in channel bindings. For example, a mechanism may
verify that the initiator address field of the channel binding
contains the correct network address of the host system. Portable
applications should therefore ensure that they either provide correct
information for the address fields, or omit setting of the addressing
information.

The caller initiating the security context must determine the
appropriate channel binding values to set in the GSSContext object.
The acceptor must provide an identical binding in order to validate
that received tokens possess correct channel-related characteristics.

Use of channel bindings is optional in GSS-API. ChannelBinding can be
set for the

GSSContext

using the

setChannelBinding

method
before the first call to

initSecContext

or

acceptSecContext

has been performed. Unless the

setChannelBinding

method has been used to set the ChannelBinding for a GSSContext object,

null

ChannelBinding will be assumed.

Conceptually, the GSS-API concatenates the initiator and acceptor
address information, and the application supplied byte array to form an
octet string. The mechanism calculates a MIC over this octet string and
binds the MIC to the context establishment token emitted by

initSecContext

method of the

GSSContext

interface. The same bindings are set by the context acceptor for its

GSSContext

object and during processing of the

acceptSecContext

method a MIC is calculated in the same
way. The calculated MIC is compared with that found in the token, and if
the MICs differ, accept will throw a

GSSException

with the
major code set to

BAD_BINDINGS

, and
the context will not be established. Some mechanisms may include the
actual channel binding data in the token (rather than just a MIC);
applications should therefore not use confidential data as
channel-binding components.

Individual mechanisms may impose additional constraints on addresses
that may appear in channel bindings. For example, a mechanism may
verify that the initiator address field of the channel binding
contains the correct network address of the host system. Portable
applications should therefore ensure that they either provide correct
information for the address fields, or omit setting of the addressing
information.

Use of channel bindings is optional in GSS-API. ChannelBinding can be
set for the

GSSContext

using the

setChannelBinding

method
before the first call to

initSecContext

or

acceptSecContext

has been performed. Unless the

setChannelBinding

method has been used to set the ChannelBinding for a GSSContext object,

null

ChannelBinding will be assumed.

Conceptually, the GSS-API concatenates the initiator and acceptor
address information, and the application supplied byte array to form an
octet string. The mechanism calculates a MIC over this octet string and
binds the MIC to the context establishment token emitted by

initSecContext

method of the

GSSContext

interface. The same bindings are set by the context acceptor for its

GSSContext

object and during processing of the

acceptSecContext

method a MIC is calculated in the same
way. The calculated MIC is compared with that found in the token, and if
the MICs differ, accept will throw a

GSSException

with the
major code set to

BAD_BINDINGS

, and
the context will not be established. Some mechanisms may include the
actual channel binding data in the token (rather than just a MIC);
applications should therefore not use confidential data as
channel-binding components.

Individual mechanisms may impose additional constraints on addresses
that may appear in channel bindings. For example, a mechanism may
verify that the initiator address field of the channel binding
contains the correct network address of the host system. Portable
applications should therefore ensure that they either provide correct
information for the address fields, or omit setting of the addressing
information.

Conceptually, the GSS-API concatenates the initiator and acceptor
address information, and the application supplied byte array to form an
octet string. The mechanism calculates a MIC over this octet string and
binds the MIC to the context establishment token emitted by

initSecContext

method of the

GSSContext

interface. The same bindings are set by the context acceptor for its

GSSContext

object and during processing of the

acceptSecContext

method a MIC is calculated in the same
way. The calculated MIC is compared with that found in the token, and if
the MICs differ, accept will throw a

GSSException

with the
major code set to

BAD_BINDINGS

, and
the context will not be established. Some mechanisms may include the
actual channel binding data in the token (rather than just a MIC);
applications should therefore not use confidential data as
channel-binding components.

Individual mechanisms may impose additional constraints on addresses
that may appear in channel bindings. For example, a mechanism may
verify that the initiator address field of the channel binding
contains the correct network address of the host system. Portable
applications should therefore ensure that they either provide correct
information for the address fields, or omit setting of the addressing
information.

Individual mechanisms may impose additional constraints on addresses
that may appear in channel bindings. For example, a mechanism may
verify that the initiator address field of the channel binding
contains the correct network address of the host system. Portable
applications should therefore ensure that they either provide correct
information for the address fields, or omit setting of the addressing
information.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ChannelBinding

​(byte[] appData)

Creates a ChannelBinding object without any addressing information.

ChannelBinding

​(

InetAddress

initAddr,

InetAddress

acceptAddr,
byte[] appData)

Create a ChannelBinding object with user supplied address information
and data.

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

obj)

Compares two instances of ChannelBinding.

InetAddress

getAcceptorAddress

()

Get the acceptor's address for this channel binding.

byte[]

getApplicationData

()

Get the application specified data for this channel binding.

InetAddress

getInitiatorAddress

()

Get the initiator's address for this channel binding.

int

hashCode

()

Returns a hashcode value for this ChannelBinding object.

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

ChannelBinding

​(byte[] appData)

Creates a ChannelBinding object without any addressing information.

ChannelBinding

​(

InetAddress

initAddr,

InetAddress

acceptAddr,
byte[] appData)

Create a ChannelBinding object with user supplied address information
and data.

---

#### Constructor Summary

Creates a ChannelBinding object without any addressing information.

Create a ChannelBinding object with user supplied address information
and data.

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

obj)

Compares two instances of ChannelBinding.

InetAddress

getAcceptorAddress

()

Get the acceptor's address for this channel binding.

byte[]

getApplicationData

()

Get the application specified data for this channel binding.

InetAddress

getInitiatorAddress

()

Get the initiator's address for this channel binding.

int

hashCode

()

Returns a hashcode value for this ChannelBinding object.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Compares two instances of ChannelBinding.

Get the acceptor's address for this channel binding.

Get the application specified data for this channel binding.

Get the initiator's address for this channel binding.

Returns a hashcode value for this ChannelBinding object.

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

- ChannelBinding

```java
public ChannelBinding​(
InetAddress
initAddr,

InetAddress
acceptAddr,
byte[] appData)
```

Create a ChannelBinding object with user supplied address information
and data.

null

values can be used for any fields which the
application does not want to specify.

**Parameters:** initAddr

- the address of the context initiator.

null

value can be supplied to indicate that the
application does not want to set this value.
**Parameters:** acceptAddr

- the address of the context
acceptor.

null

value can be supplied to indicate that
the application does not want to set this value.
**Parameters:** appData

- application supplied data to be used as part of the
channel bindings.

null

value can be supplied to
indicate that the application does not want to set this value.

- ChannelBinding

```java
public ChannelBinding​(byte[] appData)
```

Creates a ChannelBinding object without any addressing information.

**Parameters:** appData

- application supplied data to be used as part of the
channel bindings.

============ METHOD DETAIL ==========

- Method Detail

- getInitiatorAddress

```java
public
InetAddress
getInitiatorAddress()
```

Get the initiator's address for this channel binding.

**Returns:** the initiator's address.

null

is returned if
the address has not been set.

- getAcceptorAddress

```java
public
InetAddress
getAcceptorAddress()
```

Get the acceptor's address for this channel binding.

**Returns:** the acceptor's address. null is returned if the address has
not been set.

- getApplicationData

```java
public byte[] getApplicationData()
```

Get the application specified data for this channel binding.

**Returns:** the application data being used as part of the
ChannelBinding.

null

is returned if no application data
has been specified for the channel binding.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two instances of ChannelBinding.

**Overrides:** equals

in class

Object
**Parameters:** obj

- another ChannelBinding to compare this one with
**Returns:** true if the two ChannelBinding's contain
the same values for the initiator and acceptor addresses and the
application data.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hashcode value for this ChannelBinding object.

**Overrides:** hashCode

in class

Object
**Returns:** a hashCode value
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- ChannelBinding

```java
public ChannelBinding​(
InetAddress
initAddr,

InetAddress
acceptAddr,
byte[] appData)
```

Create a ChannelBinding object with user supplied address information
and data.

null

values can be used for any fields which the
application does not want to specify.

**Parameters:** initAddr

- the address of the context initiator.

null

value can be supplied to indicate that the
application does not want to set this value.
**Parameters:** acceptAddr

- the address of the context
acceptor.

null

value can be supplied to indicate that
the application does not want to set this value.
**Parameters:** appData

- application supplied data to be used as part of the
channel bindings.

null

value can be supplied to
indicate that the application does not want to set this value.

- ChannelBinding

```java
public ChannelBinding​(byte[] appData)
```

Creates a ChannelBinding object without any addressing information.

**Parameters:** appData

- application supplied data to be used as part of the
channel bindings.

---

#### Constructor Detail

ChannelBinding

```java
public ChannelBinding​(
InetAddress
initAddr,

InetAddress
acceptAddr,
byte[] appData)
```

Create a ChannelBinding object with user supplied address information
and data.

null

values can be used for any fields which the
application does not want to specify.

**Parameters:** initAddr

- the address of the context initiator.

null

value can be supplied to indicate that the
application does not want to set this value.
**Parameters:** acceptAddr

- the address of the context
acceptor.

null

value can be supplied to indicate that
the application does not want to set this value.
**Parameters:** appData

- application supplied data to be used as part of the
channel bindings.

null

value can be supplied to
indicate that the application does not want to set this value.

---

#### ChannelBinding

public ChannelBinding​(

InetAddress

initAddr,

InetAddress

acceptAddr,
byte[] appData)

Create a ChannelBinding object with user supplied address information
and data.

null

values can be used for any fields which the
application does not want to specify.

ChannelBinding

```java
public ChannelBinding​(byte[] appData)
```

Creates a ChannelBinding object without any addressing information.

**Parameters:** appData

- application supplied data to be used as part of the
channel bindings.

---

#### ChannelBinding

public ChannelBinding​(byte[] appData)

Creates a ChannelBinding object without any addressing information.

Method Detail

- getInitiatorAddress

```java
public
InetAddress
getInitiatorAddress()
```

Get the initiator's address for this channel binding.

**Returns:** the initiator's address.

null

is returned if
the address has not been set.

- getAcceptorAddress

```java
public
InetAddress
getAcceptorAddress()
```

Get the acceptor's address for this channel binding.

**Returns:** the acceptor's address. null is returned if the address has
not been set.

- getApplicationData

```java
public byte[] getApplicationData()
```

Get the application specified data for this channel binding.

**Returns:** the application data being used as part of the
ChannelBinding.

null

is returned if no application data
has been specified for the channel binding.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two instances of ChannelBinding.

**Overrides:** equals

in class

Object
**Parameters:** obj

- another ChannelBinding to compare this one with
**Returns:** true if the two ChannelBinding's contain
the same values for the initiator and acceptor addresses and the
application data.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hashcode value for this ChannelBinding object.

**Overrides:** hashCode

in class

Object
**Returns:** a hashCode value
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getInitiatorAddress

```java
public
InetAddress
getInitiatorAddress()
```

Get the initiator's address for this channel binding.

**Returns:** the initiator's address.

null

is returned if
the address has not been set.

---

#### getInitiatorAddress

public

InetAddress

getInitiatorAddress()

Get the initiator's address for this channel binding.

getAcceptorAddress

```java
public
InetAddress
getAcceptorAddress()
```

Get the acceptor's address for this channel binding.

**Returns:** the acceptor's address. null is returned if the address has
not been set.

---

#### getAcceptorAddress

public

InetAddress

getAcceptorAddress()

Get the acceptor's address for this channel binding.

getApplicationData

```java
public byte[] getApplicationData()
```

Get the application specified data for this channel binding.

**Returns:** the application data being used as part of the
ChannelBinding.

null

is returned if no application data
has been specified for the channel binding.

---

#### getApplicationData

public byte[] getApplicationData()

Get the application specified data for this channel binding.

equals

```java
public boolean equals​(
Object
obj)
```

Compares two instances of ChannelBinding.

**Overrides:** equals

in class

Object
**Parameters:** obj

- another ChannelBinding to compare this one with
**Returns:** true if the two ChannelBinding's contain
the same values for the initiator and acceptor addresses and the
application data.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares two instances of ChannelBinding.

hashCode

```java
public int hashCode()
```

Returns a hashcode value for this ChannelBinding object.

**Overrides:** hashCode

in class

Object
**Returns:** a hashCode value
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode value for this ChannelBinding object.

---

