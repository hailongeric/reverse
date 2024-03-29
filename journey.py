#!/usr/bin/python
import subprocess

def read_key(arch):
  with open("keys.backup") as f:
    ln = [k for k in f.read().splitlines() if arch in k][0]
  return ln[ln.find(": ") + 2:].strip()

def merge(keys):
  assert len(set([len(k) for k in keys])) == 1
  res = bytearray(len(keys[0]))

  keys = [bytearray(k) for k in keys]

  for i in xrange(len(keys[0])):
    for k in keys:
      res[i] ^= k[i]

  return res

def journey(arch):
  print "++ Journey to %s" % arch.upper()
  key = read_key(arch.upper())
  if len(key) != 32:
    print "Incorrect key length."
    return

  try:
    key.decode("hex")
  except TypeError:
    print "Incorrect key format."
    return

  p = subprocess.Popen(
      ["./payload_%s.elf" % arch],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE)
  stdoutdata, stderrdata = p.communicate(key + "\n")
  if stderrdata:
    print stderrdata.strip()
  if stdoutdata:
    print stdoutdata.strip()

  print

  if "journey completed" in stdoutdata:
    return key.decode('hex')

  return

keys = [journey(arch) for arch in ["x86"]]
#keys = [journey(arch) for arch in ["arm", "mips", "x86", "ppc", "sparc", "s390"]]

if all(keys):
  print "Flag:", merge(keys)



