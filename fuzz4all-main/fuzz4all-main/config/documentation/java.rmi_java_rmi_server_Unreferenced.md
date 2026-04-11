# Interface Unreferenced

**Source:** `java.rmi\java\rmi\server\Unreferenced.html`

### Class Description

```java
public interface
Unreferenced
```

A remote object implementation should implement the

Unreferenced

interface to receive notification when there are
no more clients that reference that remote object.

**All Known Implementing Classes:** RMIConnectionImpl

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void unreferenced()

Called by the RMI runtime sometime after the runtime determines that
the reference list, the list of clients referencing the remote object,
becomes empty.

**Since:**
- 1.1

---

### Additional Sections

#### Interface Unreferenced

**All Known Implementing Classes:** RMIConnectionImpl

```java
public interface
Unreferenced
```

A remote object implementation should implement the

Unreferenced

interface to receive notification when there are
no more clients that reference that remote object.

**Since:** 1.1

public interface

Unreferenced

A remote object implementation should implement the

Unreferenced

interface to receive notification when there are
no more clients that reference that remote object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

unreferenced

()

Called by the RMI runtime sometime after the runtime determines that
the reference list, the list of clients referencing the remote object,
becomes empty.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

unreferenced

()

Called by the RMI runtime sometime after the runtime determines that
the reference list, the list of clients referencing the remote object,
becomes empty.

---

#### Method Summary

Called by the RMI runtime sometime after the runtime determines that
the reference list, the list of clients referencing the remote object,
becomes empty.

============ METHOD DETAIL ==========

- Method Detail

- unreferenced

```java
void unreferenced()
```

Called by the RMI runtime sometime after the runtime determines that
the reference list, the list of clients referencing the remote object,
becomes empty.

**Since:** 1.1

Method Detail

- unreferenced

```java
void unreferenced()
```

Called by the RMI runtime sometime after the runtime determines that
the reference list, the list of clients referencing the remote object,
becomes empty.

**Since:** 1.1

---

#### Method Detail

unreferenced

```java
void unreferenced()
```

Called by the RMI runtime sometime after the runtime determines that
the reference list, the list of clients referencing the remote object,
becomes empty.

**Since:** 1.1

---

#### unreferenced

void unreferenced()

Called by the RMI runtime sometime after the runtime determines that
the reference list, the list of clients referencing the remote object,
becomes empty.

---

