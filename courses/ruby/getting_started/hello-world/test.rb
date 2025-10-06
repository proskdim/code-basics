result = hello()
expected = 'Hello, World!'
if result != expected
  puts "Expected: #{expected}, got: #{result}"
  exit 1
end
puts 'OK'
