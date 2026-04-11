# Interface WindowConstants

**Source:** `java.desktop\javax\swing\WindowConstants.html`

### Class Description

```java
public interface
WindowConstants
```

Constants used to control the window-closing operation.
The

setDefaultCloseOperation

and

getDefaultCloseOperation

methods
provided by

JFrame

,

JInternalFrame

, and

JDialog

use these constants.
For examples of setting the default window-closing operation, see

Responding to Window-Closing Events

,
a section in

The Java Tutorial

.

**All Known Implementing Classes:** JDialog

,

JFrame

,

JInternalFrame

---

### Field Details

#### static final int DO_NOTHING_ON_CLOSE

The do-nothing default window close operation.

**See Also:**
- Constant Field Values

---

#### static final int HIDE_ON_CLOSE

The hide-window default window close operation

**See Also:**
- Constant Field Values

---

#### static final int DISPOSE_ON_CLOSE

The dispose-window default window close operation.

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**See Also:**
- Window.dispose()

,

JInternalFrame.dispose()

,

Constant Field Values

---

#### static final int EXIT_ON_CLOSE

The exit application default window close operation. Attempting
to set this on Windows that support this, such as

JFrame

, may throw a

SecurityException

based
on the

SecurityManager

.
It is recommended you only use this in an application.

**See Also:**
- JFrame.setDefaultCloseOperation(int)

,

Constant Field Values

**Since:**
- 1.4

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface WindowConstants

**All Known Implementing Classes:** JDialog

,

JFrame

,

JInternalFrame

```java
public interface
WindowConstants
```

Constants used to control the window-closing operation.
The

setDefaultCloseOperation

and

getDefaultCloseOperation

methods
provided by

JFrame

,

JInternalFrame

, and

JDialog

use these constants.
For examples of setting the default window-closing operation, see

Responding to Window-Closing Events

,
a section in

The Java Tutorial

.

**Since:** 1.2
**See Also:** JFrame.setDefaultCloseOperation(int)

,

JDialog.setDefaultCloseOperation(int)

,

JInternalFrame.setDefaultCloseOperation(int)

public interface

WindowConstants

Constants used to control the window-closing operation.
The

setDefaultCloseOperation

and

getDefaultCloseOperation

methods
provided by

JFrame

,

JInternalFrame

, and

JDialog

use these constants.
For examples of setting the default window-closing operation, see

Responding to Window-Closing Events

,
a section in

The Java Tutorial

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

DISPOSE_ON_CLOSE

The dispose-window default window close operation.

static int

DO_NOTHING_ON_CLOSE

The do-nothing default window close operation.

static int

EXIT_ON_CLOSE

The exit application default window close operation.

static int

HIDE_ON_CLOSE

The hide-window default window close operation

Field Summary

Fields

Modifier and Type

Field

Description

static int

DISPOSE_ON_CLOSE

The dispose-window default window close operation.

static int

DO_NOTHING_ON_CLOSE

The do-nothing default window close operation.

static int

EXIT_ON_CLOSE

The exit application default window close operation.

static int

HIDE_ON_CLOSE

The hide-window default window close operation

---

#### Field Summary

The dispose-window default window close operation.

The do-nothing default window close operation.

The exit application default window close operation.

The hide-window default window close operation

============ FIELD DETAIL ===========

- Field Detail

- DO_NOTHING_ON_CLOSE

```java
static final int DO_NOTHING_ON_CLOSE
```

The do-nothing default window close operation.

**See Also:** Constant Field Values

- HIDE_ON_CLOSE

```java
static final int HIDE_ON_CLOSE
```

The hide-window default window close operation

**See Also:** Constant Field Values

- DISPOSE_ON_CLOSE

```java
static final int DISPOSE_ON_CLOSE
```

The dispose-window default window close operation.

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**See Also:** Window.dispose()

,

JInternalFrame.dispose()

,

Constant Field Values

- EXIT_ON_CLOSE

```java
static final int EXIT_ON_CLOSE
```

The exit application default window close operation. Attempting
to set this on Windows that support this, such as

JFrame

, may throw a

SecurityException

based
on the

SecurityManager

.
It is recommended you only use this in an application.

**Since:** 1.4
**See Also:** JFrame.setDefaultCloseOperation(int)

,

Constant Field Values

Field Detail

- DO_NOTHING_ON_CLOSE

```java
static final int DO_NOTHING_ON_CLOSE
```

The do-nothing default window close operation.

**See Also:** Constant Field Values

- HIDE_ON_CLOSE

```java
static final int HIDE_ON_CLOSE
```

The hide-window default window close operation

**See Also:** Constant Field Values

- DISPOSE_ON_CLOSE

```java
static final int DISPOSE_ON_CLOSE
```

The dispose-window default window close operation.

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**See Also:** Window.dispose()

,

JInternalFrame.dispose()

,

Constant Field Values

- EXIT_ON_CLOSE

```java
static final int EXIT_ON_CLOSE
```

The exit application default window close operation. Attempting
to set this on Windows that support this, such as

JFrame

, may throw a

SecurityException

based
on the

SecurityManager

.
It is recommended you only use this in an application.

**Since:** 1.4
**See Also:** JFrame.setDefaultCloseOperation(int)

,

Constant Field Values

---

#### Field Detail

DO_NOTHING_ON_CLOSE

```java
static final int DO_NOTHING_ON_CLOSE
```

The do-nothing default window close operation.

**See Also:** Constant Field Values

---

#### DO_NOTHING_ON_CLOSE

static final int DO_NOTHING_ON_CLOSE

The do-nothing default window close operation.

HIDE_ON_CLOSE

```java
static final int HIDE_ON_CLOSE
```

The hide-window default window close operation

**See Also:** Constant Field Values

---

#### HIDE_ON_CLOSE

static final int HIDE_ON_CLOSE

The hide-window default window close operation

DISPOSE_ON_CLOSE

```java
static final int DISPOSE_ON_CLOSE
```

The dispose-window default window close operation.

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**See Also:** Window.dispose()

,

JInternalFrame.dispose()

,

Constant Field Values

---

#### DISPOSE_ON_CLOSE

static final int DISPOSE_ON_CLOSE

The dispose-window default window close operation.

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

Note

: When the last displayable window
within the Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

EXIT_ON_CLOSE

```java
static final int EXIT_ON_CLOSE
```

The exit application default window close operation. Attempting
to set this on Windows that support this, such as

JFrame

, may throw a

SecurityException

based
on the

SecurityManager

.
It is recommended you only use this in an application.

**Since:** 1.4
**See Also:** JFrame.setDefaultCloseOperation(int)

,

Constant Field Values

---

#### EXIT_ON_CLOSE

static final int EXIT_ON_CLOSE

The exit application default window close operation. Attempting
to set this on Windows that support this, such as

JFrame

, may throw a

SecurityException

based
on the

SecurityManager

.
It is recommended you only use this in an application.

---

