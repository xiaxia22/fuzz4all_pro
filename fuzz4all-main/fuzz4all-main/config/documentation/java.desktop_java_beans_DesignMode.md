# Interface DesignMode

**Source:** `java.desktop\java\beans\DesignMode.html`

### Class Description

```java
public interface
DesignMode
```

This interface is intended to be implemented by, or delegated from, instances
of java.beans.beancontext.BeanContext, in order to propagate to its nested hierarchy
of java.beans.beancontext.BeanContextChild instances, the current "designTime" property.

The JavaBeans™ specification defines the notion of design time as is a
mode in which JavaBeans instances should function during their composition
and customization in a interactive design, composition or construction tool,
as opposed to runtime when the JavaBean is part of an applet, application,
or other live Java executable abstraction.

**All Known Subinterfaces:** BeanContext

,

BeanContextServices

---

### Field Details

#### static final
String
PROPERTYNAME

The standard value of the propertyName as fired from a BeanContext or
other source of PropertyChangeEvents.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void setDesignTime​(boolean designTime)

Sets the "value" of the "designTime" property.

If the implementing object is an instance of java.beans.beancontext.BeanContext,
or a subinterface thereof, then that BeanContext should fire a
PropertyChangeEvent, to its registered BeanContextMembershipListeners, with
parameters:

- propertyName

-

java.beans.DesignMode.PROPERTYNAME

oldValue

- previous value of "designTime"

newValue

- current value of "designTime"

Note it is illegal for a BeanContextChild to invoke this method
associated with a BeanContext that it is nested within.

**Parameters:**
- designTime

- the current "value" of the "designTime" property

**See Also:**
- BeanContext

,

BeanContextMembershipListener

,

PropertyChangeEvent

---

#### boolean isDesignTime()

A value of true denotes that JavaBeans should behave in design time
mode, a value of false denotes runtime behavior.

**Returns:**
- the current "value" of the "designTime" property.

---

### Additional Sections

#### Interface DesignMode

**All Known Subinterfaces:** BeanContext

,

BeanContextServices

**All Known Implementing Classes:** BeanContextServicesSupport

,

BeanContextSupport

```java
public interface
DesignMode
```

This interface is intended to be implemented by, or delegated from, instances
of java.beans.beancontext.BeanContext, in order to propagate to its nested hierarchy
of java.beans.beancontext.BeanContextChild instances, the current "designTime" property.

The JavaBeans™ specification defines the notion of design time as is a
mode in which JavaBeans instances should function during their composition
and customization in a interactive design, composition or construction tool,
as opposed to runtime when the JavaBean is part of an applet, application,
or other live Java executable abstraction.

**Since:** 1.2
**See Also:** BeanContext

,

BeanContextChild

,

BeanContextMembershipListener

,

PropertyChangeEvent

public interface

DesignMode

This interface is intended to be implemented by, or delegated from, instances
of java.beans.beancontext.BeanContext, in order to propagate to its nested hierarchy
of java.beans.beancontext.BeanContextChild instances, the current "designTime" property.

The JavaBeans™ specification defines the notion of design time as is a
mode in which JavaBeans instances should function during their composition
and customization in a interactive design, composition or construction tool,
as opposed to runtime when the JavaBean is part of an applet, application,
or other live Java executable abstraction.

The JavaBeans™ specification defines the notion of design time as is a
mode in which JavaBeans instances should function during their composition
and customization in a interactive design, composition or construction tool,
as opposed to runtime when the JavaBean is part of an applet, application,
or other live Java executable abstraction.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

PROPERTYNAME

The standard value of the propertyName as fired from a BeanContext or
other source of PropertyChangeEvents.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isDesignTime

()

A value of true denotes that JavaBeans should behave in design time
mode, a value of false denotes runtime behavior.

void

setDesignTime

​(boolean designTime)

Sets the "value" of the "designTime" property.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

PROPERTYNAME

The standard value of the propertyName as fired from a BeanContext or
other source of PropertyChangeEvents.

---

#### Field Summary

The standard value of the propertyName as fired from a BeanContext or
other source of PropertyChangeEvents.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isDesignTime

()

A value of true denotes that JavaBeans should behave in design time
mode, a value of false denotes runtime behavior.

void

setDesignTime

​(boolean designTime)

Sets the "value" of the "designTime" property.

---

#### Method Summary

A value of true denotes that JavaBeans should behave in design time
mode, a value of false denotes runtime behavior.

Sets the "value" of the "designTime" property.

============ FIELD DETAIL ===========

- Field Detail

- PROPERTYNAME

```java
static final
String
PROPERTYNAME
```

The standard value of the propertyName as fired from a BeanContext or
other source of PropertyChangeEvents.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- setDesignTime

```java
void setDesignTime​(boolean designTime)
```

Sets the "value" of the "designTime" property.

If the implementing object is an instance of java.beans.beancontext.BeanContext,
or a subinterface thereof, then that BeanContext should fire a
PropertyChangeEvent, to its registered BeanContextMembershipListeners, with
parameters:

- propertyName

-

java.beans.DesignMode.PROPERTYNAME

oldValue

- previous value of "designTime"

newValue

- current value of "designTime"

Note it is illegal for a BeanContextChild to invoke this method
associated with a BeanContext that it is nested within.

**Parameters:** designTime

- the current "value" of the "designTime" property
**See Also:** BeanContext

,

BeanContextMembershipListener

,

PropertyChangeEvent

- isDesignTime

```java
boolean isDesignTime()
```

A value of true denotes that JavaBeans should behave in design time
mode, a value of false denotes runtime behavior.

**Returns:** the current "value" of the "designTime" property.

Field Detail

- PROPERTYNAME

```java
static final
String
PROPERTYNAME
```

The standard value of the propertyName as fired from a BeanContext or
other source of PropertyChangeEvents.

**See Also:** Constant Field Values

---

#### Field Detail

PROPERTYNAME

```java
static final
String
PROPERTYNAME
```

The standard value of the propertyName as fired from a BeanContext or
other source of PropertyChangeEvents.

**See Also:** Constant Field Values

---

#### PROPERTYNAME

static final

String

PROPERTYNAME

The standard value of the propertyName as fired from a BeanContext or
other source of PropertyChangeEvents.

Method Detail

- setDesignTime

```java
void setDesignTime​(boolean designTime)
```

Sets the "value" of the "designTime" property.

If the implementing object is an instance of java.beans.beancontext.BeanContext,
or a subinterface thereof, then that BeanContext should fire a
PropertyChangeEvent, to its registered BeanContextMembershipListeners, with
parameters:

- propertyName

-

java.beans.DesignMode.PROPERTYNAME

oldValue

- previous value of "designTime"

newValue

- current value of "designTime"

Note it is illegal for a BeanContextChild to invoke this method
associated with a BeanContext that it is nested within.

**Parameters:** designTime

- the current "value" of the "designTime" property
**See Also:** BeanContext

,

BeanContextMembershipListener

,

PropertyChangeEvent

- isDesignTime

```java
boolean isDesignTime()
```

A value of true denotes that JavaBeans should behave in design time
mode, a value of false denotes runtime behavior.

**Returns:** the current "value" of the "designTime" property.

---

#### Method Detail

setDesignTime

```java
void setDesignTime​(boolean designTime)
```

Sets the "value" of the "designTime" property.

If the implementing object is an instance of java.beans.beancontext.BeanContext,
or a subinterface thereof, then that BeanContext should fire a
PropertyChangeEvent, to its registered BeanContextMembershipListeners, with
parameters:

- propertyName

-

java.beans.DesignMode.PROPERTYNAME

oldValue

- previous value of "designTime"

newValue

- current value of "designTime"

Note it is illegal for a BeanContextChild to invoke this method
associated with a BeanContext that it is nested within.

**Parameters:** designTime

- the current "value" of the "designTime" property
**See Also:** BeanContext

,

BeanContextMembershipListener

,

PropertyChangeEvent

---

#### setDesignTime

void setDesignTime​(boolean designTime)

Sets the "value" of the "designTime" property.

If the implementing object is an instance of java.beans.beancontext.BeanContext,
or a subinterface thereof, then that BeanContext should fire a
PropertyChangeEvent, to its registered BeanContextMembershipListeners, with
parameters:

- propertyName

-

java.beans.DesignMode.PROPERTYNAME

oldValue

- previous value of "designTime"

newValue

- current value of "designTime"

Note it is illegal for a BeanContextChild to invoke this method
associated with a BeanContext that it is nested within.

If the implementing object is an instance of java.beans.beancontext.BeanContext,
or a subinterface thereof, then that BeanContext should fire a
PropertyChangeEvent, to its registered BeanContextMembershipListeners, with
parameters:

- propertyName

-

java.beans.DesignMode.PROPERTYNAME

oldValue

- previous value of "designTime"

newValue

- current value of "designTime"

Note it is illegal for a BeanContextChild to invoke this method
associated with a BeanContext that it is nested within.

propertyName

-

java.beans.DesignMode.PROPERTYNAME

oldValue

- previous value of "designTime"

newValue

- current value of "designTime"

isDesignTime

```java
boolean isDesignTime()
```

A value of true denotes that JavaBeans should behave in design time
mode, a value of false denotes runtime behavior.

**Returns:** the current "value" of the "designTime" property.

---

#### isDesignTime

boolean isDesignTime()

A value of true denotes that JavaBeans should behave in design time
mode, a value of false denotes runtime behavior.

---

