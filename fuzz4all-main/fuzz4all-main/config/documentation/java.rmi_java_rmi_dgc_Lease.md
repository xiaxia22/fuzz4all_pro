# Class Lease

**Source:** `java.rmi\java\rmi\dgc\Lease.html`

### Class Description

```java
public final class
Lease

extends
Object

implements
Serializable
```

A lease contains a unique VM identifier and a lease duration. A
Lease object is used to request and grant leases to remote object
references.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Lease​(
VMID
id,
long duration)

Constructs a lease with a specific VMID and lease duration. The
vmid may be null.

**Parameters:**
- id

- VMID associated with this lease
- duration

- lease duration

---

### Method Details

#### public
VMID
getVMID()

Returns the client VMID associated with the lease.

**Returns:**
- client VMID

---

#### public long getValue()

Returns the lease duration.

**Returns:**
- lease duration

---

### Additional Sections

#### Class Lease

java.lang.Object

- java.rmi.dgc.Lease

java.rmi.dgc.Lease

**All Implemented Interfaces:** Serializable

```java
public final class
Lease

extends
Object

implements
Serializable
```

A lease contains a unique VM identifier and a lease duration. A
Lease object is used to request and grant leases to remote object
references.

**See Also:** Serialized Form

public final class

Lease

extends

Object

implements

Serializable

A lease contains a unique VM identifier and a lease duration. A
Lease object is used to request and grant leases to remote object
references.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Lease

​(

VMID

id,
long duration)

Constructs a lease with a specific VMID and lease duration.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getValue

()

Returns the lease duration.

VMID

getVMID

()

Returns the client VMID associated with the lease.

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

Lease

​(

VMID

id,
long duration)

Constructs a lease with a specific VMID and lease duration.

---

#### Constructor Summary

Constructs a lease with a specific VMID and lease duration.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getValue

()

Returns the lease duration.

VMID

getVMID

()

Returns the client VMID associated with the lease.

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

Returns the lease duration.

Returns the client VMID associated with the lease.

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

- Lease

```java
public Lease​(
VMID
id,
long duration)
```

Constructs a lease with a specific VMID and lease duration. The
vmid may be null.

**Parameters:** id

- VMID associated with this lease
**Parameters:** duration

- lease duration

============ METHOD DETAIL ==========

- Method Detail

- getVMID

```java
public
VMID
getVMID()
```

Returns the client VMID associated with the lease.

**Returns:** client VMID

- getValue

```java
public long getValue()
```

Returns the lease duration.

**Returns:** lease duration

Constructor Detail

- Lease

```java
public Lease​(
VMID
id,
long duration)
```

Constructs a lease with a specific VMID and lease duration. The
vmid may be null.

**Parameters:** id

- VMID associated with this lease
**Parameters:** duration

- lease duration

---

#### Constructor Detail

Lease

```java
public Lease​(
VMID
id,
long duration)
```

Constructs a lease with a specific VMID and lease duration. The
vmid may be null.

**Parameters:** id

- VMID associated with this lease
**Parameters:** duration

- lease duration

---

#### Lease

public Lease​(

VMID

id,
long duration)

Constructs a lease with a specific VMID and lease duration. The
vmid may be null.

Method Detail

- getVMID

```java
public
VMID
getVMID()
```

Returns the client VMID associated with the lease.

**Returns:** client VMID

- getValue

```java
public long getValue()
```

Returns the lease duration.

**Returns:** lease duration

---

#### Method Detail

getVMID

```java
public
VMID
getVMID()
```

Returns the client VMID associated with the lease.

**Returns:** client VMID

---

#### getVMID

public

VMID

getVMID()

Returns the client VMID associated with the lease.

getValue

```java
public long getValue()
```

Returns the lease duration.

**Returns:** lease duration

---

#### getValue

public long getValue()

Returns the lease duration.

---

