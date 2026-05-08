export const CATS = [
  {
    id: 'bufis', folderKey: 'BufferedInputStream', display: 'BufferedInputStream', short: 'BufIS',
    badge: 'b-res', tagTxt: 'RESOURCE', module: 'java.base',
    fullName: 'java.io.BufferedInputStream', profile: 'resource_buffer_batch', desc: '缓冲输入流',
    allTags: ['RESOURCE', 'BUFFER', 'MARK_SUPPORT'],
    total: 60, safe: 24, fail: 36, err: 0, to: 0
  },
  {
    id: 'file', folderKey: 'java_io_File', display: 'File', short: 'File',
    badge: 'b-file', tagTxt: 'FILE', module: 'java.base',
    fullName: 'java.io.File', profile: 'file_path_state', desc: '文件系统操作',
    allTags: ['FILE', 'RESOURCE'],
    total: 50, safe: 27, fail: 23, err: 0, to: 0
  },
  {
    id: 'thread', folderKey: 'java_lang_Thread', display: 'Thread', short: 'Thread',
    badge: 'b-conc', tagTxt: 'CONCURRENT', module: 'java.base',
    fullName: 'java.lang.Thread', profile: 'concurrent_sequence', desc: '线程管理',
    allTags: ['CONCURRENT', 'CALLBACK'],
    total: 50, safe: 35, fail: 15, err: 0, to: 0
  },
  {
    id: 'method', folderKey: 'java_lang_reflect_Method', display: 'Method (Reflect)', short: 'Method',
    badge: 'b-refl', tagTxt: 'REFLECT', module: 'java.base',
    fullName: 'java.lang.reflect.Method', profile: 'reflection_dispatch', desc: '方法反射调用',
    allTags: ['REFLECT', 'UTILITY'],
    total: 60, safe: 30, fail: 30, err: 0, to: 0
  },
  {
    id: 'socket', folderKey: 'java_net_Socket', display: 'Socket', short: 'Socket',
    badge: 'b-net', tagTxt: 'NETWORK', module: 'java.base',
    fullName: 'java.net.Socket', profile: 'network_endpoint_state', desc: '网络Socket',
    allTags: ['NETWORK', 'RESOURCE'],
    total: 60, safe: 30, fail: 30, err: 0, to: 0
  },
  {
    id: 'uri', folderKey: 'java_net_URI', display: 'URI', short: 'URI',
    badge: 'b-net', tagTxt: 'NETWORK', module: 'java.base',
    fullName: 'java.net.URI', profile: 'network_endpoint_state', desc: 'URI解析操作',
    allTags: ['NETWORK', 'UTILITY'],
    total: 60, safe: 40, fail: 15, err: 5, to: 0
  },
  {
    id: 'dur', folderKey: 'java_time_Duration', display: 'Duration', short: 'Duration',
    badge: 'b-time', tagTxt: 'TIME', module: 'java.base',
    fullName: 'java.time.Duration', profile: 'time_boundary_mix', desc: '时间段计算',
    allTags: ['TIME', 'UTILITY'],
    total: 60, safe: 40, fail: 20, err: 0, to: 0
  },
  {
    id: 'cipher', folderKey: 'javax_crypto_Cipher', display: 'Cipher', short: 'Cipher',
    badge: 'b-sec', tagTxt: 'SECURITY', module: 'java.base',
    fullName: 'javax.crypto.Cipher', profile: 'security_provider_flow', desc: '加密解密',
    allTags: ['SECURITY', 'UTILITY'],
    total: 50, safe: 23, fail: 27, err: 0, to: 0
  },
  {
    id: 'pcs', folderKey: 'java_beans_PropertyChangeSupport', display: 'PropertyChangeSupport', short: 'PCS',
    badge: 'b-cb', tagTxt: 'CALLBACK', module: 'java.desktop',
    fullName: 'java.beans.PropertyChangeSupport', profile: 'callback_registration_flow', desc: '属性变更监听',
    allTags: ['CALLBACK', 'UTILITY'],
    total: 60, safe: 9, fail: 51, err: 0, to: 0
  },
  {
    id: 'jmgt', folderKey: 'ManagementFactory', display: 'ManagementFactory', short: 'JMgt',
    badge: 'b-jvm', tagTxt: 'JVM_MGMT', module: 'java.management',
    fullName: 'java.lang.management.ManagementFactory', profile: 'jvm_mgmt_runtime_state', desc: 'JVM运行时管理',
    allTags: ['JVM_MGMT', 'UTILITY'],
    total: 60, safe: 39, fail: 21, err: 0, to: 0
  },
]

export function tagColor (t) {
  const m = {
    SECURITY: 'var(--red)', REFLECT: 'var(--purple)', FILE: 'var(--green)', CONCURRENT: 'var(--orange)',
    NETWORK: 'var(--primary)', CALLBACK: '#6D28D9', TIME: 'var(--teal)', JVM_MGMT: 'var(--green)',
    RESOURCE: '#92400E', BUFFER: '#92400E', MARK_SUPPORT: '#0891B2', UTILITY: 'var(--muted)', GENERIC: 'var(--muted)'
  }
  return m[t] || 'var(--muted)'
}

export function tagBg (t) {
  const m = {
    SECURITY: 'var(--red-l)', REFLECT: 'var(--purple-l)', FILE: 'var(--green-l)', CONCURRENT: 'var(--orange-l)',
    NETWORK: 'var(--primary-l)', CALLBACK: '#EDE9FE', TIME: 'var(--teal-l)', JVM_MGMT: 'var(--green-l)',
    RESOURCE: '#FEF3C7', BUFFER: '#FEF3C7', MARK_SUPPORT: 'var(--teal-l)', UTILITY: 'var(--border)', GENERIC: 'var(--border)'
  }
  return m[t] || 'var(--border)'
}
