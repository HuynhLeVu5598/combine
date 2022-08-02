if read_2000 == b'\xc0\x00\x02\x00\x19\x00\x00\x01\x00`\x01\x01\x00@\x00%':  # gia tri 37
if read_4000 == b'\xc0\x00\x02\x00\x19\x00\x00\x01\x00`\x01\x01\x00\x00\x00\x05':  # gia tri 5
def memory_area_write(self,memory_area_code,beginning_address=b'\x00\x00\x00', write_bytes=b'', number_of_items=0):

    assert len(beginning_address)==3
	data = memory_area_code+beginning_address+number_of_items.to_bytes(2,'big')+write_bytes
	response=self.execute_fins_command_frame(
		self.fins_command_frame(FinsCommandCode().MEMORY_AREA_WRITE,data))
	return response
