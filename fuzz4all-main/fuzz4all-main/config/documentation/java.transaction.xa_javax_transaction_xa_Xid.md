# Interface Xid

**Source:** `java.transaction.xa\javax\transaction\xa\Xid.html`

### Class Description

```java
public interface
Xid
```

The Xid interface is a Java mapping of the X/Open transaction identifier
XID structure. This interface specifies three accessor methods to
retrieve a global transaction format ID, global transaction ID,
and branch qualifier. The Xid interface is used by the transaction
manager and the resource managers. This interface is not visible to
the application programs.

**Since:** 1.4

---

### Field Details

#### static final int MAXGTRIDSIZE

Maximum number of bytes returned by

getGlobalTransactionId()

.

**See Also:**
- Constant Field Values

---

#### static final int MAXBQUALSIZE

Maximum number of bytes returned by

getBranchQualifier()

.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getFormatId()

Obtain the format identifier part of the XID.

**Returns:**
- Format identifier. O means the OSI CCR format.

---

#### byte[] getGlobalTransactionId()

Obtain the global transaction identifier part of XID as an array
of bytes.

**Returns:**
- Global transaction identifier.

---

#### byte[] getBranchQualifier()

Obtain the transaction branch identifier part of XID as an array
of bytes.

**Returns:**
- Global transaction identifier.

---

### Additional Sections

#### Interface Xid

```java
public interface
Xid
```

The Xid interface is a Java mapping of the X/Open transaction identifier
XID structure. This interface specifies three accessor methods to
retrieve a global transaction format ID, global transaction ID,
and branch qualifier. The Xid interface is used by the transaction
manager and the resource managers. This interface is not visible to
the application programs.

**Since:** 1.4

public interface

Xid

The Xid interface is a Java mapping of the X/Open transaction identifier
XID structure. This interface specifies three accessor methods to
retrieve a global transaction format ID, global transaction ID,
and branch qualifier. The Xid interface is used by the transaction
manager and the resource managers. This interface is not visible to
the application programs.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

MAXBQUALSIZE

Maximum number of bytes returned by

getBranchQualifier()

.

static int

MAXGTRIDSIZE

Maximum number of bytes returned by

getGlobalTransactionId()

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

byte[]

getBranchQualifier

()

Obtain the transaction branch identifier part of XID as an array
of bytes.

int

getFormatId

()

Obtain the format identifier part of the XID.

byte[]

getGlobalTransactionId

()

Obtain the global transaction identifier part of XID as an array
of bytes.

Field Summary

Fields

Modifier and Type

Field

Description

static int

MAXBQUALSIZE

Maximum number of bytes returned by

getBranchQualifier()

.

static int

MAXGTRIDSIZE

Maximum number of bytes returned by

getGlobalTransactionId()

.

---

#### Field Summary

Maximum number of bytes returned by

getBranchQualifier()

.

Maximum number of bytes returned by

getGlobalTransactionId()

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

byte[]

getBranchQualifier

()

Obtain the transaction branch identifier part of XID as an array
of bytes.

int

getFormatId

()

Obtain the format identifier part of the XID.

byte[]

getGlobalTransactionId

()

Obtain the global transaction identifier part of XID as an array
of bytes.

---

#### Method Summary

Obtain the transaction branch identifier part of XID as an array
of bytes.

Obtain the format identifier part of the XID.

Obtain the global transaction identifier part of XID as an array
of bytes.

============ FIELD DETAIL ===========

- Field Detail

- MAXGTRIDSIZE

```java
static final int MAXGTRIDSIZE
```

Maximum number of bytes returned by

getGlobalTransactionId()

.

**See Also:** Constant Field Values

- MAXBQUALSIZE

```java
static final int MAXBQUALSIZE
```

Maximum number of bytes returned by

getBranchQualifier()

.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getFormatId

```java
int getFormatId()
```

Obtain the format identifier part of the XID.

**Returns:** Format identifier. O means the OSI CCR format.

- getGlobalTransactionId

```java
byte[] getGlobalTransactionId()
```

Obtain the global transaction identifier part of XID as an array
of bytes.

**Returns:** Global transaction identifier.

- getBranchQualifier

```java
byte[] getBranchQualifier()
```

Obtain the transaction branch identifier part of XID as an array
of bytes.

**Returns:** Global transaction identifier.

Field Detail

- MAXGTRIDSIZE

```java
static final int MAXGTRIDSIZE
```

Maximum number of bytes returned by

getGlobalTransactionId()

.

**See Also:** Constant Field Values

- MAXBQUALSIZE

```java
static final int MAXBQUALSIZE
```

Maximum number of bytes returned by

getBranchQualifier()

.

**See Also:** Constant Field Values

---

#### Field Detail

MAXGTRIDSIZE

```java
static final int MAXGTRIDSIZE
```

Maximum number of bytes returned by

getGlobalTransactionId()

.

**See Also:** Constant Field Values

---

#### MAXGTRIDSIZE

static final int MAXGTRIDSIZE

Maximum number of bytes returned by

getGlobalTransactionId()

.

MAXBQUALSIZE

```java
static final int MAXBQUALSIZE
```

Maximum number of bytes returned by

getBranchQualifier()

.

**See Also:** Constant Field Values

---

#### MAXBQUALSIZE

static final int MAXBQUALSIZE

Maximum number of bytes returned by

getBranchQualifier()

.

Method Detail

- getFormatId

```java
int getFormatId()
```

Obtain the format identifier part of the XID.

**Returns:** Format identifier. O means the OSI CCR format.

- getGlobalTransactionId

```java
byte[] getGlobalTransactionId()
```

Obtain the global transaction identifier part of XID as an array
of bytes.

**Returns:** Global transaction identifier.

- getBranchQualifier

```java
byte[] getBranchQualifier()
```

Obtain the transaction branch identifier part of XID as an array
of bytes.

**Returns:** Global transaction identifier.

---

#### Method Detail

getFormatId

```java
int getFormatId()
```

Obtain the format identifier part of the XID.

**Returns:** Format identifier. O means the OSI CCR format.

---

#### getFormatId

int getFormatId()

Obtain the format identifier part of the XID.

getGlobalTransactionId

```java
byte[] getGlobalTransactionId()
```

Obtain the global transaction identifier part of XID as an array
of bytes.

**Returns:** Global transaction identifier.

---

#### getGlobalTransactionId

byte[] getGlobalTransactionId()

Obtain the global transaction identifier part of XID as an array
of bytes.

getBranchQualifier

```java
byte[] getBranchQualifier()
```

Obtain the transaction branch identifier part of XID as an array
of bytes.

**Returns:** Global transaction identifier.

---

#### getBranchQualifier

byte[] getBranchQualifier()

Obtain the transaction branch identifier part of XID as an array
of bytes.

---

