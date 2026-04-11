# Class Association

**Source:** `jdk.sctp\com\sun\nio\sctp\Association.html`

### Class Description

```java
public class
Association

extends
Object
```

A class that represents an SCTP association.

An association exists between two SCTP endpoints. Each endpoint is
represented by a list of transport addresses through which that endpoint can
be reached and from which it will originate SCTP messages. The association
spans over all of the possible source/destination combinations which may be
generated from each endpoint's lists of addresses.

Associations are identified by their Association ID.
Association ID's are guaranteed to be unique for the lifetime of the
association. An association ID may be reused after the association has been
shutdown. An association ID is not unique across multiple SCTP channels.
An Association's local and remote addresses may change if the SCTP
implementation supports

Dynamic Address Reconfiguration

as defined by

RFC5061

, see the

bindAddress

and

unbindAddress

methods of

SctpChannel

,

SctpServerChannel

, and

SctpMultiChannel

.

An

Association

is returned from an

SctpChannel

or an

SctpMultiChannel

, as well
as being given as a parameter to

NotificationHandler

methods.

**Since:** 1.7

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Association​(int associationID,
int maxInStreams,
int maxOutStreams)

Initializes a new instance of this class.

**Parameters:**
- associationID

- The association ID
- maxInStreams

- The maximum number of inbound streams
- maxOutStreams

- The maximum number of outbound streams

---

### Method Details

#### public final int associationID()

Returns the associationID.

**Returns:**
- The association ID

---

#### public final int maxInboundStreams()

Returns the maximum number of inbound streams that this association
supports.

Data received on this association will be on stream number

s

, where

0 <= s < maxInboundStreams()

.

**Returns:**
- The maximum number of inbound streams

---

#### public final int maxOutboundStreams()

Returns the maximum number of outbound streams that this association
supports.

Data sent on this association must be on stream number

s

, where

0 <= s < maxOutboundStreams()

.

**Returns:**
- The maximum number of outbound streams

---

### Additional Sections

#### Class Association

java.lang.Object

- com.sun.nio.sctp.Association

com.sun.nio.sctp.Association

```java
public class
Association

extends
Object
```

A class that represents an SCTP association.

An association exists between two SCTP endpoints. Each endpoint is
represented by a list of transport addresses through which that endpoint can
be reached and from which it will originate SCTP messages. The association
spans over all of the possible source/destination combinations which may be
generated from each endpoint's lists of addresses.

Associations are identified by their Association ID.
Association ID's are guaranteed to be unique for the lifetime of the
association. An association ID may be reused after the association has been
shutdown. An association ID is not unique across multiple SCTP channels.
An Association's local and remote addresses may change if the SCTP
implementation supports

Dynamic Address Reconfiguration

as defined by

RFC5061

, see the

bindAddress

and

unbindAddress

methods of

SctpChannel

,

SctpServerChannel

, and

SctpMultiChannel

.

An

Association

is returned from an

SctpChannel

or an

SctpMultiChannel

, as well
as being given as a parameter to

NotificationHandler

methods.

**Since:** 1.7

public class

Association

extends

Object

A class that represents an SCTP association.

An association exists between two SCTP endpoints. Each endpoint is
represented by a list of transport addresses through which that endpoint can
be reached and from which it will originate SCTP messages. The association
spans over all of the possible source/destination combinations which may be
generated from each endpoint's lists of addresses.

Associations are identified by their Association ID.
Association ID's are guaranteed to be unique for the lifetime of the
association. An association ID may be reused after the association has been
shutdown. An association ID is not unique across multiple SCTP channels.
An Association's local and remote addresses may change if the SCTP
implementation supports

Dynamic Address Reconfiguration

as defined by

RFC5061

, see the

bindAddress

and

unbindAddress

methods of

SctpChannel

,

SctpServerChannel

, and

SctpMultiChannel

.

An

Association

is returned from an

SctpChannel

or an

SctpMultiChannel

, as well
as being given as a parameter to

NotificationHandler

methods.

An association exists between two SCTP endpoints. Each endpoint is
represented by a list of transport addresses through which that endpoint can
be reached and from which it will originate SCTP messages. The association
spans over all of the possible source/destination combinations which may be
generated from each endpoint's lists of addresses.

Associations are identified by their Association ID.
Association ID's are guaranteed to be unique for the lifetime of the
association. An association ID may be reused after the association has been
shutdown. An association ID is not unique across multiple SCTP channels.
An Association's local and remote addresses may change if the SCTP
implementation supports

Dynamic Address Reconfiguration

as defined by

RFC5061

, see the

bindAddress

and

unbindAddress

methods of

SctpChannel

,

SctpServerChannel

, and

SctpMultiChannel

.

An

Association

is returned from an

SctpChannel

or an

SctpMultiChannel

, as well
as being given as a parameter to

NotificationHandler

methods.

Associations are identified by their Association ID.
Association ID's are guaranteed to be unique for the lifetime of the
association. An association ID may be reused after the association has been
shutdown. An association ID is not unique across multiple SCTP channels.
An Association's local and remote addresses may change if the SCTP
implementation supports

Dynamic Address Reconfiguration

as defined by

RFC5061

, see the

bindAddress

and

unbindAddress

methods of

SctpChannel

,

SctpServerChannel

, and

SctpMultiChannel

.

An

Association

is returned from an

SctpChannel

or an

SctpMultiChannel

, as well
as being given as a parameter to

NotificationHandler

methods.

An

Association

is returned from an

SctpChannel

or an

SctpMultiChannel

, as well
as being given as a parameter to

NotificationHandler

methods.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Association

​(int associationID,
int maxInStreams,
int maxOutStreams)

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

associationID

()

Returns the associationID.

int

maxInboundStreams

()

Returns the maximum number of inbound streams that this association
supports.

int

maxOutboundStreams

()

Returns the maximum number of outbound streams that this association
supports.

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

Modifier

Constructor

Description

protected

Association

​(int associationID,
int maxInStreams,
int maxOutStreams)

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

associationID

()

Returns the associationID.

int

maxInboundStreams

()

Returns the maximum number of inbound streams that this association
supports.

int

maxOutboundStreams

()

Returns the maximum number of outbound streams that this association
supports.

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

Returns the associationID.

Returns the maximum number of inbound streams that this association
supports.

Returns the maximum number of outbound streams that this association
supports.

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

- Association

```java
protected Association​(int associationID,
int maxInStreams,
int maxOutStreams)
```

Initializes a new instance of this class.

**Parameters:** associationID

- The association ID
**Parameters:** maxInStreams

- The maximum number of inbound streams
**Parameters:** maxOutStreams

- The maximum number of outbound streams

============ METHOD DETAIL ==========

- Method Detail

- associationID

```java
public final int associationID()
```

Returns the associationID.

**Returns:** The association ID

- maxInboundStreams

```java
public final int maxInboundStreams()
```

Returns the maximum number of inbound streams that this association
supports.

Data received on this association will be on stream number

s

, where

0 <= s < maxInboundStreams()

.

**Returns:** The maximum number of inbound streams

- maxOutboundStreams

```java
public final int maxOutboundStreams()
```

Returns the maximum number of outbound streams that this association
supports.

Data sent on this association must be on stream number

s

, where

0 <= s < maxOutboundStreams()

.

**Returns:** The maximum number of outbound streams

Constructor Detail

- Association

```java
protected Association​(int associationID,
int maxInStreams,
int maxOutStreams)
```

Initializes a new instance of this class.

**Parameters:** associationID

- The association ID
**Parameters:** maxInStreams

- The maximum number of inbound streams
**Parameters:** maxOutStreams

- The maximum number of outbound streams

---

#### Constructor Detail

Association

```java
protected Association​(int associationID,
int maxInStreams,
int maxOutStreams)
```

Initializes a new instance of this class.

**Parameters:** associationID

- The association ID
**Parameters:** maxInStreams

- The maximum number of inbound streams
**Parameters:** maxOutStreams

- The maximum number of outbound streams

---

#### Association

protected Association​(int associationID,
int maxInStreams,
int maxOutStreams)

Initializes a new instance of this class.

Method Detail

- associationID

```java
public final int associationID()
```

Returns the associationID.

**Returns:** The association ID

- maxInboundStreams

```java
public final int maxInboundStreams()
```

Returns the maximum number of inbound streams that this association
supports.

Data received on this association will be on stream number

s

, where

0 <= s < maxInboundStreams()

.

**Returns:** The maximum number of inbound streams

- maxOutboundStreams

```java
public final int maxOutboundStreams()
```

Returns the maximum number of outbound streams that this association
supports.

Data sent on this association must be on stream number

s

, where

0 <= s < maxOutboundStreams()

.

**Returns:** The maximum number of outbound streams

---

#### Method Detail

associationID

```java
public final int associationID()
```

Returns the associationID.

**Returns:** The association ID

---

#### associationID

public final int associationID()

Returns the associationID.

maxInboundStreams

```java
public final int maxInboundStreams()
```

Returns the maximum number of inbound streams that this association
supports.

Data received on this association will be on stream number

s

, where

0 <= s < maxInboundStreams()

.

**Returns:** The maximum number of inbound streams

---

#### maxInboundStreams

public final int maxInboundStreams()

Returns the maximum number of inbound streams that this association
supports.

Data received on this association will be on stream number

s

, where

0 <= s < maxInboundStreams()

.

Data received on this association will be on stream number

s

, where

0 <= s < maxInboundStreams()

.

maxOutboundStreams

```java
public final int maxOutboundStreams()
```

Returns the maximum number of outbound streams that this association
supports.

Data sent on this association must be on stream number

s

, where

0 <= s < maxOutboundStreams()

.

**Returns:** The maximum number of outbound streams

---

#### maxOutboundStreams

public final int maxOutboundStreams()

Returns the maximum number of outbound streams that this association
supports.

Data sent on this association must be on stream number

s

, where

0 <= s < maxOutboundStreams()

.

Data sent on this association must be on stream number

s

, where

0 <= s < maxOutboundStreams()

.

---

