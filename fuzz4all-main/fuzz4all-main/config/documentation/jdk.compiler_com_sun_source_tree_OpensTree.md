# Interface OpensTree

**Source:** `jdk.compiler\com\sun\source\tree\OpensTree.html`

### Class Description

```java
public interface
OpensTree

extends
DirectiveTree
```

A tree node for an 'opens' directive in a module declaration.

For example:

```java
opens
package-name
;
opens
package-name
to
module-name
;
```

**All Superinterfaces:** DirectiveTree

,

Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ExpressionTree
getPackageName()

Returns the name of the package to be opened.

**Returns:**
- the name of the package to be opened

---

#### List
<? extends
ExpressionTree
> getModuleNames()

Returns the names of the modules to which the package is opened,
or null, if the package is opened to all modules.

**Returns:**
- the names of the modules to which the package is opened, or null

---

### Additional Sections

#### Interface OpensTree

**All Superinterfaces:** DirectiveTree

,

Tree

```java
public interface
OpensTree

extends
DirectiveTree
```

A tree node for an 'opens' directive in a module declaration.

For example:

```java
opens
package-name
;
opens
package-name
to
module-name
;
```

**Since:** 9

public interface

OpensTree

extends

DirectiveTree

A tree node for an 'opens' directive in a module declaration.

For example:

```java
opens
package-name
;
opens
package-name
to
module-name
;
```

opens

package-name

;
opens

package-name

to

module-name

;

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

ExpressionTree

>

getModuleNames

()

Returns the names of the modules to which the package is opened,
or null, if the package is opened to all modules.

ExpressionTree

getPackageName

()

Returns the name of the package to be opened.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested classes/interfaces declared in interface com.sun.source.tree. Tree

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

ExpressionTree

>

getModuleNames

()

Returns the names of the modules to which the package is opened,
or null, if the package is opened to all modules.

ExpressionTree

getPackageName

()

Returns the name of the package to be opened.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the names of the modules to which the package is opened,
or null, if the package is opened to all modules.

Returns the name of the package to be opened.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name of the package to be opened.

**Returns:** the name of the package to be opened

- getModuleNames

```java
List
<? extends
ExpressionTree
> getModuleNames()
```

Returns the names of the modules to which the package is opened,
or null, if the package is opened to all modules.

**Returns:** the names of the modules to which the package is opened, or null

Method Detail

- getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name of the package to be opened.

**Returns:** the name of the package to be opened

- getModuleNames

```java
List
<? extends
ExpressionTree
> getModuleNames()
```

Returns the names of the modules to which the package is opened,
or null, if the package is opened to all modules.

**Returns:** the names of the modules to which the package is opened, or null

---

#### Method Detail

getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name of the package to be opened.

**Returns:** the name of the package to be opened

---

#### getPackageName

ExpressionTree

getPackageName()

Returns the name of the package to be opened.

getModuleNames

```java
List
<? extends
ExpressionTree
> getModuleNames()
```

Returns the names of the modules to which the package is opened,
or null, if the package is opened to all modules.

**Returns:** the names of the modules to which the package is opened, or null

---

#### getModuleNames

List

<? extends

ExpressionTree

> getModuleNames()

Returns the names of the modules to which the package is opened,
or null, if the package is opened to all modules.

---

