# Class XAException

**Source:** `java.transaction.xa\javax\transaction\xa\XAException.html`

### Class Description

```java
public class
XAException

extends
Exception
```

The XAException is thrown by the Resource Manager (RM) to inform the
Transaction Manager of an error encountered by the involved transaction.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public int errorCode

The error code with which to create the SystemException.

---

#### public static final int XA_RBBASE

The inclusive lower bound of the rollback codes.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RBROLLBACK

Indicates that the rollback was caused by an unspecified reason.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RBCOMMFAIL

Indicates that the rollback was caused by a communication failure.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RBDEADLOCK

A deadlock was detected.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RBINTEGRITY

A condition that violates the integrity of the resource was detected.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RBOTHER

The resource manager rolled back the transaction branch for a reason
not on this list.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RBPROTO

A protocol error occurred in the resource manager.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RBTIMEOUT

A transaction branch took too long.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RBTRANSIENT

May retry the transaction branch.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RBEND

The inclusive upper bound of the rollback error code.

**See Also:**
- Constant Field Values

---

#### public static final int XA_NOMIGRATE

Resumption must occur where the suspension occurred.

**See Also:**
- Constant Field Values

---

#### public static final int XA_HEURHAZ

The transaction branch may have been heuristically completed.

**See Also:**
- Constant Field Values

---

#### public static final int XA_HEURCOM

The transaction branch has been heuristically committed.

**See Also:**
- Constant Field Values

---

#### public static final int XA_HEURRB

The transaction branch has been heuristically rolled back.

**See Also:**
- Constant Field Values

---

#### public static final int XA_HEURMIX

The transaction branch has been heuristically committed and
rolled back.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RETRY

Routine returned with no effect and may be reissued.

**See Also:**
- Constant Field Values

---

#### public static final int XA_RDONLY

The transaction branch was read-only and has been committed.

**See Also:**
- Constant Field Values

---

#### public static final int XAER_ASYNC

There is an asynchronous operation already outstanding.

**See Also:**
- Constant Field Values

---

#### public static final int XAER_RMERR

A resource manager error has occurred in the transaction branch.

**See Also:**
- Constant Field Values

---

#### public static final int XAER_NOTA

The XID is not valid.

**See Also:**
- Constant Field Values

---

#### public static final int XAER_INVAL

Invalid arguments were given.

**See Also:**
- Constant Field Values

---

#### public static final int XAER_PROTO

Routine was invoked in an inproper context.

**See Also:**
- Constant Field Values

---

#### public static final int XAER_RMFAIL

Resource manager is unavailable.

**See Also:**
- Constant Field Values

---

#### public static final int XAER_DUPID

The XID already exists.

**See Also:**
- Constant Field Values

---

#### public static final int XAER_OUTSIDE

The resource manager is doing work outside a global transaction.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public XAException()

Create an XAException.

---

#### public XAException​(
String
s)

Create an XAException with a given string.

**Parameters:**
- s

- The

String

object containing the exception
message.

---

#### public XAException​(int errcode)

Create an XAException with a given error code.

**Parameters:**
- errcode

- The error code identifying the exception.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class XAException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.transaction.xa.XAException

java.lang.Throwable

- java.lang.Exception
- - javax.transaction.xa.XAException

java.lang.Exception

- javax.transaction.xa.XAException

javax.transaction.xa.XAException

**All Implemented Interfaces:** Serializable

```java
public class
XAException

extends
Exception
```

The XAException is thrown by the Resource Manager (RM) to inform the
Transaction Manager of an error encountered by the involved transaction.

**Since:** 1.4
**See Also:** Serialized Form

public class

XAException

extends

Exception

The XAException is thrown by the Resource Manager (RM) to inform the
Transaction Manager of an error encountered by the involved transaction.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

int

errorCode

The error code with which to create the SystemException.

static int

XA_HEURCOM

The transaction branch has been heuristically committed.

static int

XA_HEURHAZ

The transaction branch may have been heuristically completed.

static int

XA_HEURMIX

The transaction branch has been heuristically committed and
rolled back.

static int

XA_HEURRB

The transaction branch has been heuristically rolled back.

static int

XA_NOMIGRATE

Resumption must occur where the suspension occurred.

static int

XA_RBBASE

The inclusive lower bound of the rollback codes.

static int

XA_RBCOMMFAIL

Indicates that the rollback was caused by a communication failure.

static int

XA_RBDEADLOCK

A deadlock was detected.

static int

XA_RBEND

The inclusive upper bound of the rollback error code.

static int

XA_RBINTEGRITY

A condition that violates the integrity of the resource was detected.

static int

XA_RBOTHER

The resource manager rolled back the transaction branch for a reason
not on this list.

static int

XA_RBPROTO

A protocol error occurred in the resource manager.

static int

XA_RBROLLBACK

Indicates that the rollback was caused by an unspecified reason.

static int

XA_RBTIMEOUT

A transaction branch took too long.

static int

XA_RBTRANSIENT

May retry the transaction branch.

static int

XA_RDONLY

The transaction branch was read-only and has been committed.

static int

XA_RETRY

Routine returned with no effect and may be reissued.

static int

XAER_ASYNC

There is an asynchronous operation already outstanding.

static int

XAER_DUPID

The XID already exists.

static int

XAER_INVAL

Invalid arguments were given.

static int

XAER_NOTA

The XID is not valid.

static int

XAER_OUTSIDE

The resource manager is doing work outside a global transaction.

static int

XAER_PROTO

Routine was invoked in an inproper context.

static int

XAER_RMERR

A resource manager error has occurred in the transaction branch.

static int

XAER_RMFAIL

Resource manager is unavailable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XAException

()

Create an XAException.

XAException

​(int errcode)

Create an XAException with a given error code.

XAException

​(

String

s)

Create an XAException with a given string.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

int

errorCode

The error code with which to create the SystemException.

static int

XA_HEURCOM

The transaction branch has been heuristically committed.

static int

XA_HEURHAZ

The transaction branch may have been heuristically completed.

static int

XA_HEURMIX

The transaction branch has been heuristically committed and
rolled back.

static int

XA_HEURRB

The transaction branch has been heuristically rolled back.

static int

XA_NOMIGRATE

Resumption must occur where the suspension occurred.

static int

XA_RBBASE

The inclusive lower bound of the rollback codes.

static int

XA_RBCOMMFAIL

Indicates that the rollback was caused by a communication failure.

static int

XA_RBDEADLOCK

A deadlock was detected.

static int

XA_RBEND

The inclusive upper bound of the rollback error code.

static int

XA_RBINTEGRITY

A condition that violates the integrity of the resource was detected.

static int

XA_RBOTHER

The resource manager rolled back the transaction branch for a reason
not on this list.

static int

XA_RBPROTO

A protocol error occurred in the resource manager.

static int

XA_RBROLLBACK

Indicates that the rollback was caused by an unspecified reason.

static int

XA_RBTIMEOUT

A transaction branch took too long.

static int

XA_RBTRANSIENT

May retry the transaction branch.

static int

XA_RDONLY

The transaction branch was read-only and has been committed.

static int

XA_RETRY

Routine returned with no effect and may be reissued.

static int

XAER_ASYNC

There is an asynchronous operation already outstanding.

static int

XAER_DUPID

The XID already exists.

static int

XAER_INVAL

Invalid arguments were given.

static int

XAER_NOTA

The XID is not valid.

static int

XAER_OUTSIDE

The resource manager is doing work outside a global transaction.

static int

XAER_PROTO

Routine was invoked in an inproper context.

static int

XAER_RMERR

A resource manager error has occurred in the transaction branch.

static int

XAER_RMFAIL

Resource manager is unavailable.

---

#### Field Summary

The error code with which to create the SystemException.

The transaction branch has been heuristically committed.

The transaction branch may have been heuristically completed.

The transaction branch has been heuristically committed and
rolled back.

The transaction branch has been heuristically rolled back.

Resumption must occur where the suspension occurred.

The inclusive lower bound of the rollback codes.

Indicates that the rollback was caused by a communication failure.

A deadlock was detected.

The inclusive upper bound of the rollback error code.

A condition that violates the integrity of the resource was detected.

The resource manager rolled back the transaction branch for a reason
not on this list.

A protocol error occurred in the resource manager.

Indicates that the rollback was caused by an unspecified reason.

A transaction branch took too long.

May retry the transaction branch.

The transaction branch was read-only and has been committed.

Routine returned with no effect and may be reissued.

There is an asynchronous operation already outstanding.

The XID already exists.

Invalid arguments were given.

The XID is not valid.

The resource manager is doing work outside a global transaction.

Routine was invoked in an inproper context.

A resource manager error has occurred in the transaction branch.

Resource manager is unavailable.

Constructor Summary

Constructors

Constructor

Description

XAException

()

Create an XAException.

XAException

​(int errcode)

Create an XAException with a given error code.

XAException

​(

String

s)

Create an XAException with a given string.

---

#### Constructor Summary

Create an XAException.

Create an XAException with a given error code.

Create an XAException with a given string.

Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- errorCode

```java
public int errorCode
```

The error code with which to create the SystemException.

- XA_RBBASE

```java
public static final int XA_RBBASE
```

The inclusive lower bound of the rollback codes.

**See Also:** Constant Field Values

- XA_RBROLLBACK

```java
public static final int XA_RBROLLBACK
```

Indicates that the rollback was caused by an unspecified reason.

**See Also:** Constant Field Values

- XA_RBCOMMFAIL

```java
public static final int XA_RBCOMMFAIL
```

Indicates that the rollback was caused by a communication failure.

**See Also:** Constant Field Values

- XA_RBDEADLOCK

```java
public static final int XA_RBDEADLOCK
```

A deadlock was detected.

**See Also:** Constant Field Values

- XA_RBINTEGRITY

```java
public static final int XA_RBINTEGRITY
```

A condition that violates the integrity of the resource was detected.

**See Also:** Constant Field Values

- XA_RBOTHER

```java
public static final int XA_RBOTHER
```

The resource manager rolled back the transaction branch for a reason
not on this list.

**See Also:** Constant Field Values

- XA_RBPROTO

```java
public static final int XA_RBPROTO
```

A protocol error occurred in the resource manager.

**See Also:** Constant Field Values

- XA_RBTIMEOUT

```java
public static final int XA_RBTIMEOUT
```

A transaction branch took too long.

**See Also:** Constant Field Values

- XA_RBTRANSIENT

```java
public static final int XA_RBTRANSIENT
```

May retry the transaction branch.

**See Also:** Constant Field Values

- XA_RBEND

```java
public static final int XA_RBEND
```

The inclusive upper bound of the rollback error code.

**See Also:** Constant Field Values

- XA_NOMIGRATE

```java
public static final int XA_NOMIGRATE
```

Resumption must occur where the suspension occurred.

**See Also:** Constant Field Values

- XA_HEURHAZ

```java
public static final int XA_HEURHAZ
```

The transaction branch may have been heuristically completed.

**See Also:** Constant Field Values

- XA_HEURCOM

```java
public static final int XA_HEURCOM
```

The transaction branch has been heuristically committed.

**See Also:** Constant Field Values

- XA_HEURRB

```java
public static final int XA_HEURRB
```

The transaction branch has been heuristically rolled back.

**See Also:** Constant Field Values

- XA_HEURMIX

```java
public static final int XA_HEURMIX
```

The transaction branch has been heuristically committed and
rolled back.

**See Also:** Constant Field Values

- XA_RETRY

```java
public static final int XA_RETRY
```

Routine returned with no effect and may be reissued.

**See Also:** Constant Field Values

- XA_RDONLY

```java
public static final int XA_RDONLY
```

The transaction branch was read-only and has been committed.

**See Also:** Constant Field Values

- XAER_ASYNC

```java
public static final int XAER_ASYNC
```

There is an asynchronous operation already outstanding.

**See Also:** Constant Field Values

- XAER_RMERR

```java
public static final int XAER_RMERR
```

A resource manager error has occurred in the transaction branch.

**See Also:** Constant Field Values

- XAER_NOTA

```java
public static final int XAER_NOTA
```

The XID is not valid.

**See Also:** Constant Field Values

- XAER_INVAL

```java
public static final int XAER_INVAL
```

Invalid arguments were given.

**See Also:** Constant Field Values

- XAER_PROTO

```java
public static final int XAER_PROTO
```

Routine was invoked in an inproper context.

**See Also:** Constant Field Values

- XAER_RMFAIL

```java
public static final int XAER_RMFAIL
```

Resource manager is unavailable.

**See Also:** Constant Field Values

- XAER_DUPID

```java
public static final int XAER_DUPID
```

The XID already exists.

**See Also:** Constant Field Values

- XAER_OUTSIDE

```java
public static final int XAER_OUTSIDE
```

The resource manager is doing work outside a global transaction.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- XAException

```java
public XAException()
```

Create an XAException.

- XAException

```java
public XAException​(
String
s)
```

Create an XAException with a given string.

**Parameters:** s

- The

String

object containing the exception
message.

- XAException

```java
public XAException​(int errcode)
```

Create an XAException with a given error code.

**Parameters:** errcode

- The error code identifying the exception.

Field Detail

- errorCode

```java
public int errorCode
```

The error code with which to create the SystemException.

- XA_RBBASE

```java
public static final int XA_RBBASE
```

The inclusive lower bound of the rollback codes.

**See Also:** Constant Field Values

- XA_RBROLLBACK

```java
public static final int XA_RBROLLBACK
```

Indicates that the rollback was caused by an unspecified reason.

**See Also:** Constant Field Values

- XA_RBCOMMFAIL

```java
public static final int XA_RBCOMMFAIL
```

Indicates that the rollback was caused by a communication failure.

**See Also:** Constant Field Values

- XA_RBDEADLOCK

```java
public static final int XA_RBDEADLOCK
```

A deadlock was detected.

**See Also:** Constant Field Values

- XA_RBINTEGRITY

```java
public static final int XA_RBINTEGRITY
```

A condition that violates the integrity of the resource was detected.

**See Also:** Constant Field Values

- XA_RBOTHER

```java
public static final int XA_RBOTHER
```

The resource manager rolled back the transaction branch for a reason
not on this list.

**See Also:** Constant Field Values

- XA_RBPROTO

```java
public static final int XA_RBPROTO
```

A protocol error occurred in the resource manager.

**See Also:** Constant Field Values

- XA_RBTIMEOUT

```java
public static final int XA_RBTIMEOUT
```

A transaction branch took too long.

**See Also:** Constant Field Values

- XA_RBTRANSIENT

```java
public static final int XA_RBTRANSIENT
```

May retry the transaction branch.

**See Also:** Constant Field Values

- XA_RBEND

```java
public static final int XA_RBEND
```

The inclusive upper bound of the rollback error code.

**See Also:** Constant Field Values

- XA_NOMIGRATE

```java
public static final int XA_NOMIGRATE
```

Resumption must occur where the suspension occurred.

**See Also:** Constant Field Values

- XA_HEURHAZ

```java
public static final int XA_HEURHAZ
```

The transaction branch may have been heuristically completed.

**See Also:** Constant Field Values

- XA_HEURCOM

```java
public static final int XA_HEURCOM
```

The transaction branch has been heuristically committed.

**See Also:** Constant Field Values

- XA_HEURRB

```java
public static final int XA_HEURRB
```

The transaction branch has been heuristically rolled back.

**See Also:** Constant Field Values

- XA_HEURMIX

```java
public static final int XA_HEURMIX
```

The transaction branch has been heuristically committed and
rolled back.

**See Also:** Constant Field Values

- XA_RETRY

```java
public static final int XA_RETRY
```

Routine returned with no effect and may be reissued.

**See Also:** Constant Field Values

- XA_RDONLY

```java
public static final int XA_RDONLY
```

The transaction branch was read-only and has been committed.

**See Also:** Constant Field Values

- XAER_ASYNC

```java
public static final int XAER_ASYNC
```

There is an asynchronous operation already outstanding.

**See Also:** Constant Field Values

- XAER_RMERR

```java
public static final int XAER_RMERR
```

A resource manager error has occurred in the transaction branch.

**See Also:** Constant Field Values

- XAER_NOTA

```java
public static final int XAER_NOTA
```

The XID is not valid.

**See Also:** Constant Field Values

- XAER_INVAL

```java
public static final int XAER_INVAL
```

Invalid arguments were given.

**See Also:** Constant Field Values

- XAER_PROTO

```java
public static final int XAER_PROTO
```

Routine was invoked in an inproper context.

**See Also:** Constant Field Values

- XAER_RMFAIL

```java
public static final int XAER_RMFAIL
```

Resource manager is unavailable.

**See Also:** Constant Field Values

- XAER_DUPID

```java
public static final int XAER_DUPID
```

The XID already exists.

**See Also:** Constant Field Values

- XAER_OUTSIDE

```java
public static final int XAER_OUTSIDE
```

The resource manager is doing work outside a global transaction.

**See Also:** Constant Field Values

---

#### Field Detail

errorCode

```java
public int errorCode
```

The error code with which to create the SystemException.

---

#### errorCode

public int errorCode

The error code with which to create the SystemException.

XA_RBBASE

```java
public static final int XA_RBBASE
```

The inclusive lower bound of the rollback codes.

**See Also:** Constant Field Values

---

#### XA_RBBASE

public static final int XA_RBBASE

The inclusive lower bound of the rollback codes.

XA_RBROLLBACK

```java
public static final int XA_RBROLLBACK
```

Indicates that the rollback was caused by an unspecified reason.

**See Also:** Constant Field Values

---

#### XA_RBROLLBACK

public static final int XA_RBROLLBACK

Indicates that the rollback was caused by an unspecified reason.

XA_RBCOMMFAIL

```java
public static final int XA_RBCOMMFAIL
```

Indicates that the rollback was caused by a communication failure.

**See Also:** Constant Field Values

---

#### XA_RBCOMMFAIL

public static final int XA_RBCOMMFAIL

Indicates that the rollback was caused by a communication failure.

XA_RBDEADLOCK

```java
public static final int XA_RBDEADLOCK
```

A deadlock was detected.

**See Also:** Constant Field Values

---

#### XA_RBDEADLOCK

public static final int XA_RBDEADLOCK

A deadlock was detected.

XA_RBINTEGRITY

```java
public static final int XA_RBINTEGRITY
```

A condition that violates the integrity of the resource was detected.

**See Also:** Constant Field Values

---

#### XA_RBINTEGRITY

public static final int XA_RBINTEGRITY

A condition that violates the integrity of the resource was detected.

XA_RBOTHER

```java
public static final int XA_RBOTHER
```

The resource manager rolled back the transaction branch for a reason
not on this list.

**See Also:** Constant Field Values

---

#### XA_RBOTHER

public static final int XA_RBOTHER

The resource manager rolled back the transaction branch for a reason
not on this list.

XA_RBPROTO

```java
public static final int XA_RBPROTO
```

A protocol error occurred in the resource manager.

**See Also:** Constant Field Values

---

#### XA_RBPROTO

public static final int XA_RBPROTO

A protocol error occurred in the resource manager.

XA_RBTIMEOUT

```java
public static final int XA_RBTIMEOUT
```

A transaction branch took too long.

**See Also:** Constant Field Values

---

#### XA_RBTIMEOUT

public static final int XA_RBTIMEOUT

A transaction branch took too long.

XA_RBTRANSIENT

```java
public static final int XA_RBTRANSIENT
```

May retry the transaction branch.

**See Also:** Constant Field Values

---

#### XA_RBTRANSIENT

public static final int XA_RBTRANSIENT

May retry the transaction branch.

XA_RBEND

```java
public static final int XA_RBEND
```

The inclusive upper bound of the rollback error code.

**See Also:** Constant Field Values

---

#### XA_RBEND

public static final int XA_RBEND

The inclusive upper bound of the rollback error code.

XA_NOMIGRATE

```java
public static final int XA_NOMIGRATE
```

Resumption must occur where the suspension occurred.

**See Also:** Constant Field Values

---

#### XA_NOMIGRATE

public static final int XA_NOMIGRATE

Resumption must occur where the suspension occurred.

XA_HEURHAZ

```java
public static final int XA_HEURHAZ
```

The transaction branch may have been heuristically completed.

**See Also:** Constant Field Values

---

#### XA_HEURHAZ

public static final int XA_HEURHAZ

The transaction branch may have been heuristically completed.

XA_HEURCOM

```java
public static final int XA_HEURCOM
```

The transaction branch has been heuristically committed.

**See Also:** Constant Field Values

---

#### XA_HEURCOM

public static final int XA_HEURCOM

The transaction branch has been heuristically committed.

XA_HEURRB

```java
public static final int XA_HEURRB
```

The transaction branch has been heuristically rolled back.

**See Also:** Constant Field Values

---

#### XA_HEURRB

public static final int XA_HEURRB

The transaction branch has been heuristically rolled back.

XA_HEURMIX

```java
public static final int XA_HEURMIX
```

The transaction branch has been heuristically committed and
rolled back.

**See Also:** Constant Field Values

---

#### XA_HEURMIX

public static final int XA_HEURMIX

The transaction branch has been heuristically committed and
rolled back.

XA_RETRY

```java
public static final int XA_RETRY
```

Routine returned with no effect and may be reissued.

**See Also:** Constant Field Values

---

#### XA_RETRY

public static final int XA_RETRY

Routine returned with no effect and may be reissued.

XA_RDONLY

```java
public static final int XA_RDONLY
```

The transaction branch was read-only and has been committed.

**See Also:** Constant Field Values

---

#### XA_RDONLY

public static final int XA_RDONLY

The transaction branch was read-only and has been committed.

XAER_ASYNC

```java
public static final int XAER_ASYNC
```

There is an asynchronous operation already outstanding.

**See Also:** Constant Field Values

---

#### XAER_ASYNC

public static final int XAER_ASYNC

There is an asynchronous operation already outstanding.

XAER_RMERR

```java
public static final int XAER_RMERR
```

A resource manager error has occurred in the transaction branch.

**See Also:** Constant Field Values

---

#### XAER_RMERR

public static final int XAER_RMERR

A resource manager error has occurred in the transaction branch.

XAER_NOTA

```java
public static final int XAER_NOTA
```

The XID is not valid.

**See Also:** Constant Field Values

---

#### XAER_NOTA

public static final int XAER_NOTA

The XID is not valid.

XAER_INVAL

```java
public static final int XAER_INVAL
```

Invalid arguments were given.

**See Also:** Constant Field Values

---

#### XAER_INVAL

public static final int XAER_INVAL

Invalid arguments were given.

XAER_PROTO

```java
public static final int XAER_PROTO
```

Routine was invoked in an inproper context.

**See Also:** Constant Field Values

---

#### XAER_PROTO

public static final int XAER_PROTO

Routine was invoked in an inproper context.

XAER_RMFAIL

```java
public static final int XAER_RMFAIL
```

Resource manager is unavailable.

**See Also:** Constant Field Values

---

#### XAER_RMFAIL

public static final int XAER_RMFAIL

Resource manager is unavailable.

XAER_DUPID

```java
public static final int XAER_DUPID
```

The XID already exists.

**See Also:** Constant Field Values

---

#### XAER_DUPID

public static final int XAER_DUPID

The XID already exists.

XAER_OUTSIDE

```java
public static final int XAER_OUTSIDE
```

The resource manager is doing work outside a global transaction.

**See Also:** Constant Field Values

---

#### XAER_OUTSIDE

public static final int XAER_OUTSIDE

The resource manager is doing work outside a global transaction.

Constructor Detail

- XAException

```java
public XAException()
```

Create an XAException.

- XAException

```java
public XAException​(
String
s)
```

Create an XAException with a given string.

**Parameters:** s

- The

String

object containing the exception
message.

- XAException

```java
public XAException​(int errcode)
```

Create an XAException with a given error code.

**Parameters:** errcode

- The error code identifying the exception.

---

#### Constructor Detail

XAException

```java
public XAException()
```

Create an XAException.

---

#### XAException

public XAException()

Create an XAException.

XAException

```java
public XAException​(
String
s)
```

Create an XAException with a given string.

**Parameters:** s

- The

String

object containing the exception
message.

---

#### XAException

public XAException​(

String

s)

Create an XAException with a given string.

XAException

```java
public XAException​(int errcode)
```

Create an XAException with a given error code.

**Parameters:** errcode

- The error code identifying the exception.

---

#### XAException

public XAException​(int errcode)

Create an XAException with a given error code.

---

