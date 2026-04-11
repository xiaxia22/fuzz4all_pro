# Class ServiceUIFactory

**Source:** `java.desktop\javax\print\ServiceUIFactory.html`

### Class Description

```java
public abstract class
ServiceUIFactory

extends
Object
```

Services may optionally provide UIs which allow different styles of
interaction in different roles. One role may be end-user browsing and setting
of print options. Another role may be administering the print service.

Although the Print Service API does not presently provide standardised
support for administering a print service, monitoring of the print service is
possible and a UI may provide for private update mechanisms.

The basic design intent is to allow applications to lazily locate and
initialize services only when needed without any API dependencies except in
an environment in which they are used.

Swing UIs are preferred as they provide a more consistent L&F and
can support accessibility APIs.

Example usage:

```java
ServiceUIFactory factory = printService.getServiceUIFactory();
if (factory != null) {
JComponent swingui = (JComponent)factory.getUI(
ServiceUIFactory.MAIN_UIROLE,
ServiceUIFactory.JCOMPONENT_UI);
if (swingui != null) {
tabbedpane.add("Custom UI", swingui);
}
}
```

---

### Field Details

#### public static final
String
JCOMPONENT_UI

Denotes a UI implemented as a Swing component. The value of the string is
the fully qualified classname : "javax.swing.JComponent".

**See Also:**
- Constant Field Values

---

#### public static final
String
PANEL_UI

Denotes a UI implemented as an AWT panel. The value of the string is the
fully qualified classname : "java.awt.Panel"

**See Also:**
- Constant Field Values

---

#### public static final
String
DIALOG_UI

Denotes a UI implemented as an AWT dialog. The value of the string is the
fully qualified classname : "java.awt.Dialog"

**See Also:**
- Constant Field Values

---

#### public static final
String
JDIALOG_UI

Denotes a UI implemented as a Swing dialog. The value of the string is
the fully qualified classname : "javax.swing.JDialog"

**See Also:**
- Constant Field Values

---

#### public static final int ABOUT_UIROLE

Denotes a UI which performs an informative "About" role.

**See Also:**
- Constant Field Values

---

#### public static final int ADMIN_UIROLE

Denotes a UI which performs an administrative role.

**See Also:**
- Constant Field Values

---

#### public static final int MAIN_UIROLE

Denotes a UI which performs the normal end user role.

**See Also:**
- Constant Field Values

---

#### public static final int RESERVED_UIROLE

Not a valid role but role id's greater than this may be used for private
roles supported by a service. Knowledge of the function performed by this
role is required to make proper use of it.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ServiceUIFactory()

*No description found.*

---

### Method Details

#### public abstract
Object
getUI​(int role,

String
ui)

Get a UI object which may be cast to the requested UI type by the
application and used in its user interface.

**Parameters:**
- role

- requested. Must be one of the standard roles or a private
role supported by this factory.
- ui

- type in which the role is requested

**Returns:**
- the UI role or

null

if the requested UI role is not
available from this factory

**Throws:**
- IllegalArgumentException

- if the role or ui is neither one of the
standard ones, nor a private one supported by the factory

---

#### public abstract
String
[] getUIClassNamesForRole​(int role)

Given a UI role obtained from this factory obtain the UI types available
from this factory which implement this role. The returned

Strings

should refer to the static variables defined in this class so that
applications can use equality of reference ("==").

**Parameters:**
- role

- to be looked up

**Returns:**
- the UI types supported by this class for the specified role,

null

if no UIs are available for the role

**Throws:**
- IllegalArgumentException

- is the role is a non-standard role not
supported by this factory

---

### Additional Sections

#### Class ServiceUIFactory

java.lang.Object

- javax.print.ServiceUIFactory

javax.print.ServiceUIFactory

```java
public abstract class
ServiceUIFactory

extends
Object
```

Services may optionally provide UIs which allow different styles of
interaction in different roles. One role may be end-user browsing and setting
of print options. Another role may be administering the print service.

Although the Print Service API does not presently provide standardised
support for administering a print service, monitoring of the print service is
possible and a UI may provide for private update mechanisms.

The basic design intent is to allow applications to lazily locate and
initialize services only when needed without any API dependencies except in
an environment in which they are used.

Swing UIs are preferred as they provide a more consistent L&F and
can support accessibility APIs.

Example usage:

```java
ServiceUIFactory factory = printService.getServiceUIFactory();
if (factory != null) {
JComponent swingui = (JComponent)factory.getUI(
ServiceUIFactory.MAIN_UIROLE,
ServiceUIFactory.JCOMPONENT_UI);
if (swingui != null) {
tabbedpane.add("Custom UI", swingui);
}
}
```

public abstract class

ServiceUIFactory

extends

Object

Services may optionally provide UIs which allow different styles of
interaction in different roles. One role may be end-user browsing and setting
of print options. Another role may be administering the print service.

Although the Print Service API does not presently provide standardised
support for administering a print service, monitoring of the print service is
possible and a UI may provide for private update mechanisms.

The basic design intent is to allow applications to lazily locate and
initialize services only when needed without any API dependencies except in
an environment in which they are used.

Swing UIs are preferred as they provide a more consistent L&F and
can support accessibility APIs.

Example usage:

```java
ServiceUIFactory factory = printService.getServiceUIFactory();
if (factory != null) {
JComponent swingui = (JComponent)factory.getUI(
ServiceUIFactory.MAIN_UIROLE,
ServiceUIFactory.JCOMPONENT_UI);
if (swingui != null) {
tabbedpane.add("Custom UI", swingui);
}
}
```

Although the Print Service API does not presently provide standardised
support for administering a print service, monitoring of the print service is
possible and a UI may provide for private update mechanisms.

The basic design intent is to allow applications to lazily locate and
initialize services only when needed without any API dependencies except in
an environment in which they are used.

Swing UIs are preferred as they provide a more consistent L&F and
can support accessibility APIs.

Example usage:

```java
ServiceUIFactory factory = printService.getServiceUIFactory();
if (factory != null) {
JComponent swingui = (JComponent)factory.getUI(
ServiceUIFactory.MAIN_UIROLE,
ServiceUIFactory.JCOMPONENT_UI);
if (swingui != null) {
tabbedpane.add("Custom UI", swingui);
}
}
```

The basic design intent is to allow applications to lazily locate and
initialize services only when needed without any API dependencies except in
an environment in which they are used.

Swing UIs are preferred as they provide a more consistent L&F and
can support accessibility APIs.

Example usage:

```java
ServiceUIFactory factory = printService.getServiceUIFactory();
if (factory != null) {
JComponent swingui = (JComponent)factory.getUI(
ServiceUIFactory.MAIN_UIROLE,
ServiceUIFactory.JCOMPONENT_UI);
if (swingui != null) {
tabbedpane.add("Custom UI", swingui);
}
}
```

Swing UIs are preferred as they provide a more consistent L&F and
can support accessibility APIs.

Example usage:

```java
ServiceUIFactory factory = printService.getServiceUIFactory();
if (factory != null) {
JComponent swingui = (JComponent)factory.getUI(
ServiceUIFactory.MAIN_UIROLE,
ServiceUIFactory.JCOMPONENT_UI);
if (swingui != null) {
tabbedpane.add("Custom UI", swingui);
}
}
```

Example usage:

```java
ServiceUIFactory factory = printService.getServiceUIFactory();
if (factory != null) {
JComponent swingui = (JComponent)factory.getUI(
ServiceUIFactory.MAIN_UIROLE,
ServiceUIFactory.JCOMPONENT_UI);
if (swingui != null) {
tabbedpane.add("Custom UI", swingui);
}
}
```

ServiceUIFactory factory = printService.getServiceUIFactory();
if (factory != null) {
JComponent swingui = (JComponent)factory.getUI(
ServiceUIFactory.MAIN_UIROLE,
ServiceUIFactory.JCOMPONENT_UI);
if (swingui != null) {
tabbedpane.add("Custom UI", swingui);
}
}

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ABOUT_UIROLE

Denotes a UI which performs an informative "About" role.

static int

ADMIN_UIROLE

Denotes a UI which performs an administrative role.

static

String

DIALOG_UI

Denotes a UI implemented as an AWT dialog.

static

String

JCOMPONENT_UI

Denotes a UI implemented as a Swing component.

static

String

JDIALOG_UI

Denotes a UI implemented as a Swing dialog.

static int

MAIN_UIROLE

Denotes a UI which performs the normal end user role.

static

String

PANEL_UI

Denotes a UI implemented as an AWT panel.

static int

RESERVED_UIROLE

Not a valid role but role id's greater than this may be used for private
roles supported by a service.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ServiceUIFactory

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Object

getUI

​(int role,

String

ui)

Get a UI object which may be cast to the requested UI type by the
application and used in its user interface.

abstract

String

[]

getUIClassNamesForRole

​(int role)

Given a UI role obtained from this factory obtain the UI types available
from this factory which implement this role.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

ABOUT_UIROLE

Denotes a UI which performs an informative "About" role.

static int

ADMIN_UIROLE

Denotes a UI which performs an administrative role.

static

String

DIALOG_UI

Denotes a UI implemented as an AWT dialog.

static

String

JCOMPONENT_UI

Denotes a UI implemented as a Swing component.

static

String

JDIALOG_UI

Denotes a UI implemented as a Swing dialog.

static int

MAIN_UIROLE

Denotes a UI which performs the normal end user role.

static

String

PANEL_UI

Denotes a UI implemented as an AWT panel.

static int

RESERVED_UIROLE

Not a valid role but role id's greater than this may be used for private
roles supported by a service.

---

#### Field Summary

Denotes a UI which performs an informative "About" role.

Denotes a UI which performs an administrative role.

Denotes a UI implemented as an AWT dialog.

Denotes a UI implemented as a Swing component.

Denotes a UI implemented as a Swing dialog.

Denotes a UI which performs the normal end user role.

Denotes a UI implemented as an AWT panel.

Not a valid role but role id's greater than this may be used for private
roles supported by a service.

Constructor Summary

Constructors

Constructor

Description

ServiceUIFactory

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Object

getUI

​(int role,

String

ui)

Get a UI object which may be cast to the requested UI type by the
application and used in its user interface.

abstract

String

[]

getUIClassNamesForRole

​(int role)

Given a UI role obtained from this factory obtain the UI types available
from this factory which implement this role.

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

Get a UI object which may be cast to the requested UI type by the
application and used in its user interface.

Given a UI role obtained from this factory obtain the UI types available
from this factory which implement this role.

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

============ FIELD DETAIL ===========

- Field Detail

- JCOMPONENT_UI

```java
public static final
String
JCOMPONENT_UI
```

Denotes a UI implemented as a Swing component. The value of the string is
the fully qualified classname : "javax.swing.JComponent".

**See Also:** Constant Field Values

- PANEL_UI

```java
public static final
String
PANEL_UI
```

Denotes a UI implemented as an AWT panel. The value of the string is the
fully qualified classname : "java.awt.Panel"

**See Also:** Constant Field Values

- DIALOG_UI

```java
public static final
String
DIALOG_UI
```

Denotes a UI implemented as an AWT dialog. The value of the string is the
fully qualified classname : "java.awt.Dialog"

**See Also:** Constant Field Values

- JDIALOG_UI

```java
public static final
String
JDIALOG_UI
```

Denotes a UI implemented as a Swing dialog. The value of the string is
the fully qualified classname : "javax.swing.JDialog"

**See Also:** Constant Field Values

- ABOUT_UIROLE

```java
public static final int ABOUT_UIROLE
```

Denotes a UI which performs an informative "About" role.

**See Also:** Constant Field Values

- ADMIN_UIROLE

```java
public static final int ADMIN_UIROLE
```

Denotes a UI which performs an administrative role.

**See Also:** Constant Field Values

- MAIN_UIROLE

```java
public static final int MAIN_UIROLE
```

Denotes a UI which performs the normal end user role.

**See Also:** Constant Field Values

- RESERVED_UIROLE

```java
public static final int RESERVED_UIROLE
```

Not a valid role but role id's greater than this may be used for private
roles supported by a service. Knowledge of the function performed by this
role is required to make proper use of it.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ServiceUIFactory

```java
public ServiceUIFactory()
```

============ METHOD DETAIL ==========

- Method Detail

- getUI

```java
public abstract
Object
getUI​(int role,

String
ui)
```

Get a UI object which may be cast to the requested UI type by the
application and used in its user interface.

**Parameters:** role

- requested. Must be one of the standard roles or a private
role supported by this factory.
**Parameters:** ui

- type in which the role is requested
**Returns:** the UI role or

null

if the requested UI role is not
available from this factory
**Throws:** IllegalArgumentException

- if the role or ui is neither one of the
standard ones, nor a private one supported by the factory

- getUIClassNamesForRole

```java
public abstract
String
[] getUIClassNamesForRole​(int role)
```

Given a UI role obtained from this factory obtain the UI types available
from this factory which implement this role. The returned

Strings

should refer to the static variables defined in this class so that
applications can use equality of reference ("==").

**Parameters:** role

- to be looked up
**Returns:** the UI types supported by this class for the specified role,

null

if no UIs are available for the role
**Throws:** IllegalArgumentException

- is the role is a non-standard role not
supported by this factory

Field Detail

- JCOMPONENT_UI

```java
public static final
String
JCOMPONENT_UI
```

Denotes a UI implemented as a Swing component. The value of the string is
the fully qualified classname : "javax.swing.JComponent".

**See Also:** Constant Field Values

- PANEL_UI

```java
public static final
String
PANEL_UI
```

Denotes a UI implemented as an AWT panel. The value of the string is the
fully qualified classname : "java.awt.Panel"

**See Also:** Constant Field Values

- DIALOG_UI

```java
public static final
String
DIALOG_UI
```

Denotes a UI implemented as an AWT dialog. The value of the string is the
fully qualified classname : "java.awt.Dialog"

**See Also:** Constant Field Values

- JDIALOG_UI

```java
public static final
String
JDIALOG_UI
```

Denotes a UI implemented as a Swing dialog. The value of the string is
the fully qualified classname : "javax.swing.JDialog"

**See Also:** Constant Field Values

- ABOUT_UIROLE

```java
public static final int ABOUT_UIROLE
```

Denotes a UI which performs an informative "About" role.

**See Also:** Constant Field Values

- ADMIN_UIROLE

```java
public static final int ADMIN_UIROLE
```

Denotes a UI which performs an administrative role.

**See Also:** Constant Field Values

- MAIN_UIROLE

```java
public static final int MAIN_UIROLE
```

Denotes a UI which performs the normal end user role.

**See Also:** Constant Field Values

- RESERVED_UIROLE

```java
public static final int RESERVED_UIROLE
```

Not a valid role but role id's greater than this may be used for private
roles supported by a service. Knowledge of the function performed by this
role is required to make proper use of it.

**See Also:** Constant Field Values

---

#### Field Detail

JCOMPONENT_UI

```java
public static final
String
JCOMPONENT_UI
```

Denotes a UI implemented as a Swing component. The value of the string is
the fully qualified classname : "javax.swing.JComponent".

**See Also:** Constant Field Values

---

#### JCOMPONENT_UI

public static final

String

JCOMPONENT_UI

Denotes a UI implemented as a Swing component. The value of the string is
the fully qualified classname : "javax.swing.JComponent".

PANEL_UI

```java
public static final
String
PANEL_UI
```

Denotes a UI implemented as an AWT panel. The value of the string is the
fully qualified classname : "java.awt.Panel"

**See Also:** Constant Field Values

---

#### PANEL_UI

public static final

String

PANEL_UI

Denotes a UI implemented as an AWT panel. The value of the string is the
fully qualified classname : "java.awt.Panel"

DIALOG_UI

```java
public static final
String
DIALOG_UI
```

Denotes a UI implemented as an AWT dialog. The value of the string is the
fully qualified classname : "java.awt.Dialog"

**See Also:** Constant Field Values

---

#### DIALOG_UI

public static final

String

DIALOG_UI

Denotes a UI implemented as an AWT dialog. The value of the string is the
fully qualified classname : "java.awt.Dialog"

JDIALOG_UI

```java
public static final
String
JDIALOG_UI
```

Denotes a UI implemented as a Swing dialog. The value of the string is
the fully qualified classname : "javax.swing.JDialog"

**See Also:** Constant Field Values

---

#### JDIALOG_UI

public static final

String

JDIALOG_UI

Denotes a UI implemented as a Swing dialog. The value of the string is
the fully qualified classname : "javax.swing.JDialog"

ABOUT_UIROLE

```java
public static final int ABOUT_UIROLE
```

Denotes a UI which performs an informative "About" role.

**See Also:** Constant Field Values

---

#### ABOUT_UIROLE

public static final int ABOUT_UIROLE

Denotes a UI which performs an informative "About" role.

ADMIN_UIROLE

```java
public static final int ADMIN_UIROLE
```

Denotes a UI which performs an administrative role.

**See Also:** Constant Field Values

---

#### ADMIN_UIROLE

public static final int ADMIN_UIROLE

Denotes a UI which performs an administrative role.

MAIN_UIROLE

```java
public static final int MAIN_UIROLE
```

Denotes a UI which performs the normal end user role.

**See Also:** Constant Field Values

---

#### MAIN_UIROLE

public static final int MAIN_UIROLE

Denotes a UI which performs the normal end user role.

RESERVED_UIROLE

```java
public static final int RESERVED_UIROLE
```

Not a valid role but role id's greater than this may be used for private
roles supported by a service. Knowledge of the function performed by this
role is required to make proper use of it.

**See Also:** Constant Field Values

---

#### RESERVED_UIROLE

public static final int RESERVED_UIROLE

Not a valid role but role id's greater than this may be used for private
roles supported by a service. Knowledge of the function performed by this
role is required to make proper use of it.

Constructor Detail

- ServiceUIFactory

```java
public ServiceUIFactory()
```

---

#### Constructor Detail

ServiceUIFactory

```java
public ServiceUIFactory()
```

---

#### ServiceUIFactory

public ServiceUIFactory()

Method Detail

- getUI

```java
public abstract
Object
getUI​(int role,

String
ui)
```

Get a UI object which may be cast to the requested UI type by the
application and used in its user interface.

**Parameters:** role

- requested. Must be one of the standard roles or a private
role supported by this factory.
**Parameters:** ui

- type in which the role is requested
**Returns:** the UI role or

null

if the requested UI role is not
available from this factory
**Throws:** IllegalArgumentException

- if the role or ui is neither one of the
standard ones, nor a private one supported by the factory

- getUIClassNamesForRole

```java
public abstract
String
[] getUIClassNamesForRole​(int role)
```

Given a UI role obtained from this factory obtain the UI types available
from this factory which implement this role. The returned

Strings

should refer to the static variables defined in this class so that
applications can use equality of reference ("==").

**Parameters:** role

- to be looked up
**Returns:** the UI types supported by this class for the specified role,

null

if no UIs are available for the role
**Throws:** IllegalArgumentException

- is the role is a non-standard role not
supported by this factory

---

#### Method Detail

getUI

```java
public abstract
Object
getUI​(int role,

String
ui)
```

Get a UI object which may be cast to the requested UI type by the
application and used in its user interface.

**Parameters:** role

- requested. Must be one of the standard roles or a private
role supported by this factory.
**Parameters:** ui

- type in which the role is requested
**Returns:** the UI role or

null

if the requested UI role is not
available from this factory
**Throws:** IllegalArgumentException

- if the role or ui is neither one of the
standard ones, nor a private one supported by the factory

---

#### getUI

public abstract

Object

getUI​(int role,

String

ui)

Get a UI object which may be cast to the requested UI type by the
application and used in its user interface.

getUIClassNamesForRole

```java
public abstract
String
[] getUIClassNamesForRole​(int role)
```

Given a UI role obtained from this factory obtain the UI types available
from this factory which implement this role. The returned

Strings

should refer to the static variables defined in this class so that
applications can use equality of reference ("==").

**Parameters:** role

- to be looked up
**Returns:** the UI types supported by this class for the specified role,

null

if no UIs are available for the role
**Throws:** IllegalArgumentException

- is the role is a non-standard role not
supported by this factory

---

#### getUIClassNamesForRole

public abstract

String

[] getUIClassNamesForRole​(int role)

Given a UI role obtained from this factory obtain the UI types available
from this factory which implement this role. The returned

Strings

should refer to the static variables defined in this class so that
applications can use equality of reference ("==").

---

